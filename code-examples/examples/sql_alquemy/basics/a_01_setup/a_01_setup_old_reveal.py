#-#-#-#
"""
<section>
    <h2>Installation and Setup</h2>
</section>

<section>
    <div class="d-flex align-center justify-around">
    <div class="d-flex align-center justify-center box-1">
        <div>Test message 1</div>
    </div>
    <div class="arrow mx-6 mb-3 fragment">&#8594;</div>
    <div class="d-flex align-center justify-center box-1 fragment">
        <div>Test message 2</div>
    </div>
    </div>
</section>

<template v-for="(_, i) in ['0', '1', '2', '3', '4']">
    <section data-auto-animate :key="`a_${i}`" :data-id="i">
    <h3>What you will learn</h3>
    <br />
    <ul>
        <Li :i="i" :visible="1">Creating a virtual environment</Li>
        <Li :i="i" :visible="2">Installing sql-alchemy</Li>
        <Li :i="i" :visible="3">Verifying the installation</Li>
        <Li :i="i" :visible="4">
        Create an engine object to connect to the database
        </Li>
    </ul>
    </section>
</template>

<template v-for="(_, i) in ['0', '1', '2', '3']">
    <section data-auto-animate :key="`b_${i}`" :data-id="i">
    <h3>Generate virtualenv</h3>
    <ul>
        <Li :i="i" :visible="1">
        Generate a new folder called <code>sql_alchemy</code> and cd into
        it
        </Li>
        <Li :i="i" :visible="2">
        Generate a virtual environment with
        <code>python -m virtualenv venv</code> (if you dont have
        virtualenv installed already, run
        <code>pip install virtualenv</code>)
        </Li>
        <Li :i="i" :visible="3">
        Activate the virtual environment with
        <code>source venv/Scripts/activate</code>
        </Li>
    </ul>
    </section>
</template>

<template v-for="(_, i) in ['0', '1', '2']">
    <section data-auto-animate :key="`c_${i}`" :data-id="`c_${i}`">
    <h3>Install sql alchemy</h3>
    <ul style="list-style-type:none;">
        <Li :i="i" :visible="1">
        To install sql alchemy, run the following code in your terminal:
        </Li>
    </ul>
    <Code :visible="2" :lines="1" :i="i"
        :code="`
"""
pip install sqlalchemy
"""
    `">
    </Code>
    </section>
</template>

<template v-for="(dataLineNumbers, i) in ['0', '0', '1', '2', '3']">
    <section data-auto-animate :key="`d_${i}`" :data-id="`d_${i}`">
    <h3>Verify installation</h3>
    <h6 :class="{ opac: i < 1 }">
        To check that you have sql alchemy installed successfully:
    </h6>
    <ul>
        <Li :i="i" :visible="2">Import sql alchemy</Li>
        <Li :i="i" :visible="3">
        Check which version you have installed
        </Li>
        <Li :i="i" :visible="4">You should see our version number</Li>
    </ul>
        <Code :i="i" :visible="2" :dataLineNumbers="dataLineNumbers" :lines="3"
        :code="`
"""
import sqlalchemy
sqlalchemy.__version__
>>1.2.3            
"""
        `">
        </Code>
    </section>
</template>

<template v-for="(dataLineNumbers, i) in ['0', '1', '2', '2']">
    <section data-auto-animate :key="`e_${i}`" :data-id="`e_${i}`">
    <h3>Connect to Database with engine</h3>
    <ul>
        <li :class="{ opac: i < 1 }">Import create_engine from sqlalchemy</li>
        <li :class="{ opac: i < 2 }">
        Create a sqlite engine for a database called example.db
        </li>
    </ul>
    <Code :i="i" :visible="1" :dataLineNumbers="dataLineNumbers" :lines="2"
    :code="`
"""
from sqlalchemy import create_engine
engine = create_engine('sqlite:///example.db', echo=True)
"""
    `">
    </Code>
    <ul style="list-style-type:none;">
        <Li :i="i" :visible="3">echo=True enables logging</Li>
    </ul>
    </section>
</template>
"""
#-#-#-#
