from django.shortcuts import render
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import matplotlib
matplotlib.use('Agg')

import cv2 as cv

 
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('popular')
# nltk.download('all')

from django.contrib.staticfiles import finders




from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from A2SL.camera import VideoCamera


# Create your views here.


def home_view(request):
	return render(request,'home.html')

  
cap_device = 0 # Default device ID
cap_width = 960  # Capture width
cap_height = 540  # Capture height
use_static_image_mode = False  # Static image mode
min_detection_confidence = 0.7  # Minimum detection confidence
min_tracking_confidence = 0.5  # Minimum tracking confidence
use_brect = True  

cap = cv.VideoCapture(cap_device)
cap.set(cv.CAP_PROP_FRAME_WIDTH, cap_width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, cap_height)

def sltotext_view(request):
	return render(request, 'sltotext.html')

def gen(camera):
	while True:
		image = camera.get_image()
		yield (b'--image\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n\r\n')

def webcam_feed(request, mode=1):
	return StreamingHttpResponse(gen(VideoCamera(mode=mode)),
	                            content_type='multipart/x-mixed-replace; boundary=image')



def about_view(request):
	return render(request,'about.html')


def contact_view(request):
	return render(request,'contact.html')

# # @login_required(login_url="login")
# def animation_view(request):
# 	if request.method == 'POST':
# 		text = request.POST.get('sen')
# 		#tokenizing the sentence
# 		text.lower()
# 		#tokenizing the sentence
# 		words = word_tokenize(text)

# 		tagged = nltk.pos_tag(words)
# 		tense = {}
# 		tense["future"] = len([word for word in tagged if word[1] == "MD"])
# 		tense["present"] = len([word for word in tagged if word[1] in ["VBP", "VBZ","VBG"]])
# 		tense["past"] = len([word for word in tagged if word[1] in ["VBD", "VBN"]])
# 		tense["present_continuous"] = len([word for word in tagged if word[1] in ["VBG"]])



# 		#stopwords that will be removed
# 		stop_words = set(["mightn't", 're', 'wasn', 'wouldn', 'be', 'has', 'that', 'does', 'shouldn', 'do', "you've",'off', 'for', "didn't", 'm', 'ain', 'haven', "weren't", 'are', "she's", "wasn't", 'its', "haven't", "wouldn't", 'don', 'weren', 's', "you'd", "don't", 'doesn', "hadn't", 'is', 'was', "that'll", "should've", 'a', 'then', 'the', 'mustn', 'i', 'nor', 'as', "it's", "needn't", 'd', 'am', 'have',  'hasn', 'o', "aren't", "you'll", "couldn't", "you're", "mustn't", 'didn', "doesn't", 'll', 'an', 'hadn', 'whom', 'y', "hasn't", 'itself', 'couldn', 'needn', "shan't", 'isn', 'been', 'such', 'shan', "shouldn't", 'aren', 'being', 'were', 'did', 'ma', 't', 'having', 'mightn', 've', "isn't", "won't"])



# 		#removing stopwords and applying lemmatizing nlp process to words
# 		lr = WordNetLemmatizer()
# 		filtered_text = []
# 		for w,p in zip(words,tagged):
# 			if w not in stop_words:
# 				if p[1]=='VBG' or p[1]=='VBD' or p[1]=='VBZ' or p[1]=='VBN' or p[1]=='NN':
# 					filtered_text.append(lr.lemmatize(w,pos='v'))
# 				elif p[1]=='JJ' or p[1]=='JJR' or p[1]=='JJS'or p[1]=='RBR' or p[1]=='RBS':
# 					filtered_text.append(lr.lemmatize(w,pos='a'))

# 				else:
# 					filtered_text.append(lr.lemmatize(w))


# 		#adding the specific word to specify tense
# 		words = filtered_text
# 		temp=[]
# 		for w in words:
# 			if w=='I':
# 				temp.append('Me')
# 			else:
# 				temp.append(w)
# 		words = temp
# 		probable_tense = max(tense,key=tense.get)

# 		if probable_tense == "past" and tense["past"]>=1:
# 			temp = ["Before"]
# 			temp = temp + words
# 			words = temp
# 		elif probable_tense == "future" and tense["future"]>=1:
# 			if "Will" not in words:
# 					temp = ["Will"]
# 					temp = temp + words
# 					words = temp
# 			else:
# 				pass
# 		elif probable_tense == "present":
# 			if tense["present_continuous"]>=1:
# 				temp = ["Now"]
# 				temp = temp + words
# 				words = temp


# 		filtered_text = []
# 		for w in words:
# 			path = w + ".mp4"
# 			f = finders.find(path)
# 			#splitting the word if its animation is not present in database
# 			if not f:
# 				for c in w:
# 					filtered_text.append(c)
# 			#otherwise animation of word
# 			else:
# 				filtered_text.append(w)
# 		words = filtered_text;


# 		return render(request,'animation.html',{'words':words,'text':text})
# 	else:
# 		return render(request,'animation.html')


# def animation_view(request):
# 	if request.method == 'POST':
# 		text = request.POST.get('sen')
# 		text = text.lower()  # Make sure to assign the result back to 'text'
# 		words = word_tokenize(text)

# 		tagged = nltk.pos_tag(words)
# 		tense = {
# 			"future": len([word for word in tagged if word[1] == "MD"]),
# 			"present": len([word for word in tagged if word[1] in ["VBP", "VBZ", "VBG"]]),
# 			"past": len([word for word in tagged if word[1] in ["VBD", "VBN"]]),
# 			"present_continuous": len([word for word in tagged if word[1] in ["VBG"]]),
# 		}

# 		# ... (remaining code for tense determination and lemmatization)

# 		words_to_animate = []

# 		# First, check if the whole sentence has an animation
# 		path = f"{text}.mp4"
# 		f = finders.find(path)
# 		if f:
# 			words_to_animate.append(text)  # Append the whole sentence if animation exists
# 		else:
# 			# If whole sentence animation does not exist, then check for individual words
# 			for w in words:
# 				path = f"{w}.mp4"
# 				f = finders.find(path)  # Check if animation video exists for the word
# 				if not f:
# 					for c in w:
# 						words_to_animate.append(c)  # Split word into characters if animation doesn't exist
# 				else:
# 					words_to_animate.append(w)  # Append the word if animation exists

# 		return render(request, 'animation.html', {'words': words_to_animate, 'text': text})
# 	else:
# 		return render(request, 'animation.html')






def longest_matching_phrase(input_text):
    words = word_tokenize(input_text)
    n = len(words)
    for length in range(n, 0, -1):  # Start with the longest possible phrase and reduce
        for start in range(0, n - length + 1):
            phrase = ' '.join(words[start:start+length])
            path = f"{phrase}.mp4"
            if finders.find(path):
                return phrase  # Return the longest matching phrase
    return None  # If no phrase matches

def animation_view(request):
    if request.method == 'POST':
        text = request.POST.get('sen')
        text = text.lower()

        words_to_animate = []

        # Keep finding longest matching phrases until no words are left
        while text:
            phrase = longest_matching_phrase(text)
            if phrase:
                words_to_animate.append(phrase)
                text = text.replace(phrase, '').strip()  # Remove the matched phrase from the input
            else:
                # If no phrases match, break the loop
                break
        
        # If any words are left, handle them individually
        remaining_words = word_tokenize(text)
        for w in remaining_words:
            path = f"{w}.mp4"
            if not finders.find(path):
                for c in w:
                    words_to_animate.append(c)
            else:
                words_to_animate.append(w)

        return render(request, 'animation.html', {'words': words_to_animate, 'text': text})
    else:
        return render(request, 'animation.html')





