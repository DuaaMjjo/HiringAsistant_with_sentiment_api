
# 1. Library imports
from fastapi import FastAPI
from HirringAsistants import HirringAsistent

# 2. Create the app object
app = FastAPI()

# 3. update scores from the passed description
@app.post('/')
def update_scores(description: str):
    ha=HirringAsistent()
    inclusive_score = ha.get_inclusive_score(description)
    sentiment_score = ha.get_sentiment_score(description)
    if inclusive_score < 10:
        inclusive_suggestion= "Consider adding more diversity words."
    elif inclusive_score >= 10 and inclusive_score < 20:
        inclusive_suggestion= "Consider adding words that promote inclusion based on sexual orientation."
    else:
        inclusive_suggestion= "This looks okay and you can post it now."
    if sentiment_score == 0:
        sentiment_suggestion="Your Job description is neutral"
    else:
        sentiment_suggestion="You may consider checking the language of your description"

    return {
        'inclusive_score': inclusive_score ,
        'sentiment_score': sentiment_score,
        'inclusive_suggestion': inclusive_suggestion,
        'sentiment_suggestion':sentiment_suggestion
    }  
       
