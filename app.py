from flask import Flask, render_template, request, redirect
import openai
openai.api_key = "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"
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    feedback = ''
    message = ''
    if 'record_bt' in request.form:
        # handle button instance click
        audio_file = request.files['record_bt'].read()
        text = "I am lisenting "
        message = text
    elif 'submit_bt' in request.form:
        # handle button submit click
        text = request.form['text']
        # do something with the text, such as save it to a database or process it
        print(text)
        prompt = "You are a elementary school teacher. " \
                 "Read this passage: once upon a time there was a king who went forth into the world and fetched back a beautiful queen . and after they had been married a while god gave them a little daughter . then there was great rejoicing in the city and throughout the country , for the people wished their king all that was good , since he was kind and just . " \
                 "while the child lay in its cradle , a strange - looking old woman entered the room , and no one knew who she was nor whence she came . the old woman spoke a verse over the child , and said that she must not be allowed out under the open sky until she were full fifteen years of age , since otherwise the mountain troll would fetch her . when the king heard this he took her words to heart , " \
                 "and posted guards to watch over the little princess so that she would not get out under the open sky. " \
                 "Q:why was there great rejoicing in the city and throughout the country ?" \
                 "The kid will give an answer. Please give feedback in kids language. A:" + text
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50,
            temperature=0
        )
        generated_text = response.choices[0].text
        print(generated_text)
        message = ("Submit Successfully")
        feedback = generated_text
    else:
        feedback = "This is a Feedback"
    return render_template('index.html', text=message, feedback=feedback)

if __name__ == '__main__':
    app.run()
