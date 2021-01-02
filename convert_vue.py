
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
            if step["show_in_article"]:
                text = step["text"]
                cleanr = re.compile('<.*?>')
                text = re.sub(cleanr, '', text)
            else:
                text = ''
            audio = step["audio"]
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
    vue_base_file = open(filename_vue_file, "rt")

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
    codes_by_slide = {}
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
    for slide_number, slide in enumerate(slides, 1):
        html_slide_content_article += '<transition appear name="custom-classes-transition" enter-active-class="animated bounceIn">'
        html_slide_content_presentation += '<transition appear mode="out-in" name="custom-classes-transition" enter-active-class="animated bounceIn" leave-active-class="animated bounceOutRight">'
        html_slide_content_article += '<div>'
        html_slide_content_presentation += f'<div v-if="slide==={slide_number}" :key="{slide_number}">'
        # slide = slide.replace('\n', '')
        text_audio_codes = slide.split('#s')[1:]
        steps = []
        for step_number, text_audio_code in enumerate(text_audio_codes, 1):
            audio = None
            code = None
            data_line = None
            if '#c:' in text_audio_code:
                text_and_audio, code_and_settings = text_audio_code.split('#c:')
                settings = code_and_settings.split('\n')[0]
                code = "\n".join(code_and_settings.split('\n')[1:])
                splitted_settings = settings.split('data-line:')
                show_line = splitted_settings[0].split('show-line:')[1].strip()
                code_starts_at = min(eval(show_line))
                if len(splitted_settings) > 1:
                    data_line = splitted_settings[1].strip()
            else:
                text_and_audio = text_audio_code
            if '#audi:' in text_and_audio:
                text, audio = text_and_audio.split('#audi:')
            else:
                text = text_and_audio
            if 'h' in text.split(":")[0]:
                horizontal = True
            else:
                horizontal = False
            if 'n' in text.split(":")[0]:
                show_in_article = False
            else:
                show_in_article = True
            text = ':'.join(text.split(':')[1:])
            step = {"text": text, "audio": audio, "show_in_article": show_in_article, "horizontal": horizontal}
            output_lines_counter = 0
            if code:
                step["code"] = code
                step["show_line"] = show_line
                step["starts_at"] = code_starts_at
                code_lines = []
                for code_line in code.split('\n'):
                    code_line = code_line.replace(' ', '&nbsp;')
                    if code_line.startswith('output_file.write'):
                        code_line = ">>> " + output_file_lines[output_lines_counter].replace("\n", "")
                        output_lines_counter +=1
                    code_lines.append(code_line)
                if not slide_number in codes_by_slide:
                    codes_by_slide[slide_number] = {}
                codes_by_slide[slide_number][step_number] = code_lines
                if data_line:
                    if not slide_number in data_lines_by_slide:
                        data_lines_by_slide[slide_number] = {}
                    data_line_eval = eval(data_line)
                    data_lines_by_slide[slide_number][step_number] = data_line_eval
            steps.append(step)
        all_steps.append(steps)
        number_of_steps.append(len(steps))
        # import pdb; pdb.set_trace()
        # import pdb; pdb.set_trace()
        last_step_horizontal = False
        for step_number, step in enumerate(steps, 1):
            text = step["text"].replace('\n#', '').replace('\n', '').strip()
            audio = step["audio"]
            if len(text) > 0 and text[0] == '#':
                html_element = 'h3'
                text = text[1:]
            else:
                html_element = 'div'
            if step["show_in_article"]:
                if len(text) > 0 and text[0] == "-":
                    text_article = text[1:]
                else:
                    text_article = text
                step_html_article = '<div class="mt-2"><b><' + html_element + ' class="step-item">' + text_article + '</' + html_element + '></b></div>'
                html_slide_content_article += step_html_article
            step_html_article = '<' + html_element + ' class="step-item">' + audio + '</' + html_element + '>'
            html_slide_content_article += step_html_article

            if step["horizontal"] and not last_step_horizontal:
                html_slide_content_presentation += '<div class="d-flex">'

            step_html_presentation = '<' + html_element + ' class="step-item" :style="{visibility: step>=' + str(step_number) + ' ? \'visible\' : \'hidden\'}">' + text + '</' + html_element + '>'
            html_slide_content_presentation += step_html_presentation

            if not step["horizontal"] and last_step_horizontal:
                html_slide_content_presentation += '</div>'
            if last_step_horizontal and step_number == len(steps):
                html_slide_content_presentation += '</div>'
            last_step_horizontal = step["horizontal"]

            if "code" in step:
                step_html_article = '<pre class="language-python step-item"><code class="pl-0">' + '\n'.join(codes_by_slide[slide_number][step_number]) +'</code></pre>'
                step_html_presentation = '<pre :id="\'pre-' + str(slide_number) + '-' + str(step_number) + '\'" :ref="\'pre-' + str(slide_number) + '-' + str(step_number) +'\'" class="language-python step-item" :data-line="dataLine['+ str(step_number) +']"  :style="{visibility: step>=' + str(step["starts_at"]) + ' ? \'visible\' : \'hidden\'}" v-bind:data-show-line="JSON.stringify(' +  step["show_line"] +')"><code v-html="code['+ str(step_number) +']" class="pl-0"></code></pre>'
                html_slide_content_article += step_html_article
                html_slide_content_presentation += step_html_presentation
            if not generate_audio:
                continue
            if "audio" in step and step["audio"]:
                audio = step["audio"].replace('\n', '').strip()
                params = {"key": TEXT_TO_SPEACH_KEY}
                payload = get_payload(audio)
                res = requests.post("https://texttospeech.googleapis.com/v1/text:synthesize", data=json.dumps(payload), params=params)
                if res.ok:
                    res_body = res.json()
                    audio_content = res_body["audioContent"]
                    audio_mp3 = base64.b64decode(bytes(audio_content, 'utf-8'))
                    newFileByteArray = bytearray(audio_mp3)
                    file = open(f'./frontend/src/assets/mp3/{category_1}/{category_2}/{filename}/{slide_number}_{step_number}.mp3', 'wb')
                    file.write(newFileByteArray)
                    file.close()
        # import pdb; pdb.set_trace()
        html_slide_content_article += "</div></transition>"
        html_slide_content_presentation += "</div></transition>"

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
            vue_target_file.write(vue_line.replace("'CODE_BY_SLIDES'", str(codes_by_slide)))
        elif "CATEGORY1" in vue_line:
            vue_target_file.write(vue_line.replace("CATEGORY1", category_1))
        elif "CATEGORY2" in vue_line:
            vue_target_file.write(vue_line.replace("CATEGORY2", category_2))
        elif "FILENAME" in vue_line:
            vue_target_file.write(vue_line.replace("FILENAME", filename))
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
print(f"Filename: {filename}")
paths = Path(frontend_root_path).glob('**/*.vue')
base_vue_file = "SlideBase.vue"

for path in paths:
    if path.name == base_vue_file:
        filename_vue_file = str(path)
        print(f"Using file: {filename_vue_file}")
        replace_string(filename_vue_file)
