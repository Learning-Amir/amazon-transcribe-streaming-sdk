from flask import Flask, render_template
import asyncio

from examples.simple_mic import basic_transcribe

app = Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe')
def transcribe():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(basic_transcribe())
    loop.close()

if __name__ == '__main__':
    app.run(debug=True)
