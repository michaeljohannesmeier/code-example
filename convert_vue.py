
import os
import glob
import sys
import json
import re
from pathlib import Path

import requests
import json
import base64

from dotenv import load_dotenv
from mutagen.mp3 import MP3
load_dotenv()
TEXT_TO_SPEACH_KEY = os.getenv("TEXT_TO_SPEACH_KEY")

frontend_root_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "frontend", "src")
example_vue_path = os.path.join(frontend_root_path, "examples")
components_path = os.path.join(frontend_root_path, "components")
source_files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "code-examples", "examples")

def generate_menu():
    menu_content =  {}
    dirs_cat1 = [d for d in os.listdir(example_vue_path) if not os.path.isfile(os.path.join(example_vue_path, d))]
    for dir_cat1 in dirs_cat1:
        menu_content[dir_cat1] = {}
        dirs_cat2 = [d for d in os.listdir(os.path.join(example_vue_path, dir_cat1)) if not os.path.isfile(os.path.join(example_vue_path, dir_cat1, d))]
        for dir_cat2 in dirs_cat2:
            menu_content[dir_cat1][dir_cat2] = {}
            filenames = [d for d in os.listdir(os.path.join(example_vue_path, dir_cat1, dir_cat2)) if os.path.isfile(os.path.join(example_vue_path, dir_cat1, dir_cat2, d))]
            for filename in filenames:
                menu_content[dir_cat1][dir_cat2][filename] = filename.replace(".vue", "")

    nav_drawer_base = open(os.path.join(components_path, "NavigationDrawerBase.vue"), "rt")
    nav_drawer = open(os.path.join(components_path, "NavigationDrawer.vue"), "wt")
    for vue_line in nav_drawer_base:
        # import pdb; pdb.set_trace()
        if f"MENUCONTENT" in vue_line:
            nav_drawer.write(f"  menu = {menu_content}")
        else:
            nav_drawer.write(vue_line)
    nav_drawer.close()
    nav_drawer_base.close()

def generate_search_data(all_steps):
    search_data_path = f'./frontend/src/assets/data/search.json'
    if os.path.isfile(search_data_path):
        with open(search_data_path) as json_file:
            data = json.load(json_file)
    else:
        data = {}
    texts = ''
    for steps in all_steps:
        for step in steps:
            if step["show_text_in_article"]:
                text = step["text"]
                cleanr = re.compile('<.*?>')
                text = re.sub(cleanr, '', text)
            else:
                text = ''
            if step["show_audio_in_article"]:
                audio = step["audio"]
            else:
                audio = ''
            texts += text + "\n" + audio + "\n"
    data[f"{category_1}_{category_2}_{filename}"] = { "text": texts, "category_1": category_1, "category_2": category_2, "filename": filename }

    with open(search_data_path, 'w') as outfile:
        json.dump(data, outfile)

    data_names = []
    category1s = [d for d in os.listdir(source_files_path) if not os.path.isfile(os.path.join(source_files_path, d))]
    for category1 in category1s:
        category1_path = os.path.join(source_files_path, category1)
        category2s = [d for d in os.listdir(category1_path) if not os.path.isfile(os.path.join(category1_path, d))]
        for category2 in category2s:
            category2_path = os.path.join(category1_path, category2)
            name_folders = [d for d in os.listdir(category2_path) if not os.path.isfile(os.path.join(category2_path, d))]
            for name_folder in name_folders:
                data_name = f"{category_1}_{category_2}_{name_folder}"
                data_names.append(data_name)
                if data_name not in [d for d in data.keys()]:
                    print(f"{data_name} not found in search file yet!")
    for data_key in data.keys():
        if not data_key in data_names:
            print(f"removing {data_name} from search file!")


def replace_string(filename_vue_file):

    if not os.path.exists(os.path.join(example_vue_path, category_1)):
        os.makedirs(os.path.join(example_vue_path, category_1))
    if not os.path.exists(os.path.join(example_vue_path, category_1, category_2)):
        os.makedirs(os.path.join(example_vue_path, category_1, category_2))


    vue_target_file = open(os.path.join(example_vue_path, category_1, category_2, filename + ".vue"), "wt")
    paths = Path(source_files_path).glob('**/*.py')
    filename_source_file = None
    for path in paths:
        if path.name.split('.')[0] == f"{filename}":
            filename_source_file = str(path)
            print(f"Using source file: {filename_source_file}")
            try:
                output_file = open(os.path.join(os.path.dirname(filename_source_file), "output.txt"), "rt")
                output_file_lines = [l for l in output_file]
                output_file.close()
            except Exception:
                print("Could not find output.txt")
    if not filename_source_file:
        raise Exception("No source file found")
    source_file = open(filename_source_file, "rt")
    source_code = source_file.read()
    slides = source_code.split("#-#-#-#")[1:-1]
    html_slide_content_article = ''
    html_slide_content_presentation = ''
    number_of_steps = []
    codes_by_slides = {}
    audio_by_slides = {}
    data_lines_by_slide = {}
    if not os.path.exists(f'./frontend/src/assets/mp3/{category_1}'):
        os.makedirs(f'./frontend/src/assets/mp3/{category_1}')
    if not os.path.exists(f'./frontend/src/assets/mp3/{category_1}/{category_2}'):
        os.makedirs(f'./frontend/src/assets/mp3/{category_1}/{category_2}')
    audio_dir = f'./frontend/src/assets/mp3/{category_1}/{category_2}/{filename}'
    if not os.path.exists(audio_dir):
        os.makedirs(audio_dir)
    if generate_audio:
        file_names = [ f for f in os.listdir(audio_dir) if f.endswith(".bak") ]
        for file_name in file_names:
            os.remove(os.path.join(audio_dir, file_name))
    all_steps = []
    output_lines_counter = 0

    content_length = 0
    vue_base_file = open(filename_vue_file, "rt")
    for vue_line in vue_base_file:
        if "pauseAfterAudioFinished =" in vue_line:
            pause_after_audio_finished = int(vue_line.split("=")[1].split(";")[0]) / 1000
        if "pauseBeforeAudioStarts =" in vue_line:
            pause_before_audio_starts = int(vue_line.split("=")[1].split(";")[0]) / 1000
        if "pauseBetweenSlides =" in vue_line:
            pause_between_slides = int(vue_line.split("=")[1].split(";")[0]) / 1000
    vue_base_file.close()

    html_slide_content_presentation += '<v-carousel v-model="slide" :show-arrows="false" hide-delimiters>'
    # html_slide_content_article += '<transition appear name="custom-classes-transition" enter-active-class="animated bounceIn">'
    # html_slide_content_presentation += '<transition appear mode="out-in" name="custom-classes-transition" enter-active-class="animated bounceInRight" leave-active-class="animated bounceOutLeft">'
    for slide_number, slide in enumerate(slides, 1):
        html_slide_content_article += '<div>'
        html_slide_content_presentation += f'<v-carousel-item :key="{slide_number}">'
        # slide = slide.replace('\n', '')
        text_audio_codes = slide.split('#s')[1:]
        steps = []
        for step_number, text_audio_code in enumerate(text_audio_codes, 1):
            audio = ''
            code = None
            data_line = None
            if '#c' in text_audio_code:
                text_and_audio, code_and_settings = text_audio_code.split('#c')
                settings = code_and_settings.split('\n')[0]
                if code_and_settings.split('\n')[1][0] == "#":
                    settings+= code_and_settings.split('\n')[1].replace("#", "")
                    code = "\n".join(code_and_settings.split('\n')[2:])
                else:
                    code = "\n".join(code_and_settings.split('\n')[1:])
                splitted_settings = settings.split('data-line:')
                if "show-line:" in splitted_settings[0]:
                    show_line = splitted_settings[0].split('show-line:')[1].strip()
                    code_starts_at = min(eval(show_line))
                else:
                    show_line = "{}"
                    code_starts_at = 2
                if len(splitted_settings) > 1:
                    data_line = splitted_settings[1].strip()
            else:
                text_and_audio = text_audio_code
            if '#a' in text_and_audio:
                text, audio = text_and_audio.split('#a')
            else:
                text = text_and_audio
            if 'h' in text.split(":")[0]:
                horizontal = True
            else:
                horizontal = False
            if 'n' in text.split(":")[0]:
                show_text_in_article = False
            else:
                show_text_in_article = True
            if 'n' in audio.split(":")[0]:
                show_audio_in_article = False
            else:
                show_audio_in_article = True
            if 'o' in text.split(":")[0]:
                show_when_operator = "==="
            else:
                show_when_operator = ">="
            text = ':'.join(text.split(':')[1:])
            text = text.replace('\n#', '').replace('\n', '').strip()
            if len(text) > 0 and text[0] == '#':
                text = text[1:]
            text = re.sub(' +', ' ', text)
            audio = ':'.join(audio.split(':')[1:])
            audio = audio.replace('\n#', '').replace('\n', '').strip()
            if len(audio) > 0 and audio[0] == '#':
                audio = audio[1:]   
            if not slide_number in audio_by_slides:
                audio_by_slides[slide_number] = {}
            audio = re.sub(' +', ' ', audio)
            audio_by_slides[slide_number][step_number] = audio
            step = {"text": text, "audio": audio, "show_text_in_article": show_text_in_article, "show_audio_in_article": show_audio_in_article, "horizontal": horizontal, "show_when_operator": show_when_operator}
            if code:
                step["code"] = code
                step["show_line"] = show_line
                step["starts_at"] = code_starts_at
                code_lines = []
                for code_line in code.split('\n'):
                    code_line = code_line.replace(' ', '&nbsp;')
                    if 'output_file.write' in code_line:
                        code_line = ">>> " + output_file_lines[output_lines_counter].replace("\n", "")
                        output_lines_counter +=1
                    code_lines.append(code_line)
                if not slide_number in codes_by_slides:
                    codes_by_slides[slide_number] = {}
                codes_by_slides[slide_number][step_number] = [l.replace("<", "&lt;").replace(">", "&gt;") for l in code_lines]
                if data_line:
                    if not slide_number in data_lines_by_slide:
                        data_lines_by_slide[slide_number] = {}
                    data_line_eval = eval(data_line)
                    data_lines_by_slide[slide_number][step_number] = data_line_eval
            steps.append(step)
            if debug:
                print(step)
                print('-----')
        all_steps.append(steps)
        number_of_steps.append(len(steps))
        last_step_horizontal = False

        for step_number, step in enumerate(steps, 1):
            text = step["text"]
            audio = step["audio"]
            if step_number == 1:
                html_element = 'h3'
                classes = "mb-3"
            else:
                html_element = 'div'
                classes = ""
            if step["show_text_in_article"]:
                step_html_article = '<div class="' + classes + '"><' + html_element + ' class="step-item">' + text + '</' + html_element + '></div>'
                html_slide_content_article += step_html_article
            if step["show_audio_in_article"]:
                step_html_article = '<div class="' + classes + '"><' + html_element + ' class="step-item">' + audio + '</' + html_element + '></div>'
                html_slide_content_article += step_html_article

            if step["horizontal"] and not last_step_horizontal:
                html_slide_content_presentation += '<div class="d-flex">'
            step_html_presentation = '<' + html_element + ' class="step-item ' + classes + '" :class="{visible: step' + step["show_when_operator"] + str(step_number) + ', hidden: !(step' + step["show_when_operator"] + str(step_number) + ')}">' + text + '</' + html_element + '>'
            html_slide_content_presentation += step_html_presentation

            if not step["horizontal"] and last_step_horizontal:
                html_slide_content_presentation += '</div>'
            if last_step_horizontal and step_number == len(steps):
                html_slide_content_presentation += '</div>'
            last_step_horizontal = step["horizontal"]

            if "code" in step:
                step_html_article = '<pre class="language-python step-item line-numbers"><code class="pl-0">' + '\n'.join(codes_by_slides[slide_number][step_number]) +'</code></pre>'
                step_html_presentation = '<pre :id="\'pre-' + str(slide_number) + '-' + str(step_number) + '\'" :ref="\'pre-' + str(slide_number) + '-' + str(step_number) +'\'" class="language-python step-item" :data-line="dataLine['+ str(step_number) +']"  :class="{visible: step>=' + str(step["starts_at"]) + ', hidden: !(step>=' + str(step["starts_at"]) + ')}" v-bind:data-show-line="JSON.stringify(' +  step["show_line"] +')"><code v-html="code['+ str(step_number) +']" class="pl-0"></code></pre>'
                html_slide_content_article += step_html_article
                html_slide_content_presentation += step_html_presentation
            
            if "audio" in step and step["audio"]:
                mp3_filename = f'./frontend/src/assets/mp3/{category_1}/{category_2}/{filename}/{slide_number}_{step_number}.mp3'
                if generate_audio:
                    audio = step["audio"].replace('\n', '').replace('`', '').strip()
                    for s in [{"text": "id", "substitute": "ID"}]:
                        audio = audio.replace(f' {s["text"]} ', f' {s["substitute"]} ')
                        audio = audio.replace(f' {s["text"]}.', f' {s["substitute"]}.')
                        audio = audio.replace(f' {s["text"]},', f' {s["substitute"]},')
                        audio = audio.replace(f' {s["text"]}!', f' {s["substitute"]}!')
                        audio = audio.replace(f' {s["text"]};', f' {s["substitute"]};')
                    cleanr = re.compile('\(.*?\)')
                    audio = re.sub(cleanr, '', audio)
                    if debug:
                        print(audio)
                    params = {"key": TEXT_TO_SPEACH_KEY}
                    payload = get_payload(audio)
                    res = requests.post("https://texttospeech.googleapis.com/v1/text:synthesize", data=json.dumps(payload), params=params)
                    if res.ok:
                        res_body = res.json()
                        audio_content = res_body["audioContent"]
                        audio_mp3 = base64.b64decode(bytes(audio_content, 'utf-8'))
                        newFileByteArray = bytearray(audio_mp3)
                        file = open(mp3_filename, 'wb')
                        file.write(newFileByteArray)
                        file.close()
                    else:
                        print("Error google text to speach")
                        print(res.text)
                audio = MP3(mp3_filename)
                content_length += pause_before_audio_starts
                content_length += audio.info.length
                content_length += pause_after_audio_finished

        content_length += pause_between_slides
        # import pdb; pdb.set_trace()
        html_slide_content_presentation += "</v-carousel-item>"
        html_slide_content_article += "</div>"
    # html_slide_content_article += "</transition>"
    html_slide_content_presentation += "</v-carousel>"

    vue_base_file = open(filename_vue_file, "rt")
    for vue_line in vue_base_file:
        if f"CONTENT_ARTICLE" in vue_line:
            vue_target_file.write(html_slide_content_article)
        elif f"CONTENT_PRESENTATION" in vue_line:
            vue_target_file.write(html_slide_content_presentation)
        elif "SlideBase" in vue_line:
            vue_target_file.write(vue_line.replace("SlideBase", filename))
        elif "'NUMBER_OF_STEPS" in vue_line:
            vue_target_file.write(vue_line.replace("'NUMBER_OF_STEPS'", str(number_of_steps)))
        elif "'NUMBER_OF_SLIDES" in vue_line:
            vue_target_file.write(vue_line.replace("'NUMBER_OF_SLIDES'", str(len(slides))))
        elif "'CODE_BY_SLIDES" in vue_line:
            vue_target_file.write(vue_line.replace("'CODE_BY_SLIDES'", str(codes_by_slides)))
        elif "CATEGORY1" in vue_line:
            vue_target_file.write(vue_line.replace("CATEGORY1", category_1))
        elif "CATEGORY2" in vue_line:
            vue_target_file.write(vue_line.replace("CATEGORY2", category_2))
        elif "FILENAME" in vue_line:
            vue_target_file.write(vue_line.replace("FILENAME", filename))
        elif "CONTENT_LENGTH" in vue_line:
            vue_target_file.write(vue_line.replace("CONTENT_LENGTH", str(content_length)))
        elif "'AUDIO_BY_SLIDES'" in vue_line:
            vue_target_file.write(vue_line.replace("'AUDIO_BY_SLIDES'", str(audio_by_slides)))
        elif "'DATALINES_BY_SLIDE'" in vue_line:
            vue_target_file.write(vue_line.replace("'DATALINES_BY_SLIDE'", str(data_lines_by_slide)))
        else:
            vue_target_file.write(vue_line)
    vue_base_file.close()
    vue_target_file.close()
    generate_menu()
    generate_search_data(all_steps)


def get_payload(text):
    return {
    "input":{
      "ssml": '<speak>' + text + '</speak>'
    },
    "voice":{
      "languageCode":"en-gb",
      "name":"en-US-Wavenet-D",
      "ssmlGender":"FEMALE"
    },
    "audioConfig":{
      "audioEncoding":"MP3"
    }
  }


category_1 = sys.argv[1]
category_2 = sys.argv[2]
filename = sys.argv[3]
generate_audio = sys.argv[4] == "True"
if len(sys.argv) > 5:
    debug = sys.argv[5] == "True"
else:
    debug = False
print(f"Filename: {filename}")
paths = Path(frontend_root_path).glob('**/*.vue')
base_vue_file = "SlideBase.vue"

for path in paths:
    if path.name == base_vue_file:
        filename_vue_file = str(path)
        print(f"Using base vue file: {filename_vue_file}")
        replace_string(filename_vue_file)
