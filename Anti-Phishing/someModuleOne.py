

### Hiding things :
##  CSS : (opactity:0),(visiblity:hidden),(display:none)

### CSS : clip-path: polygon(0px 0px,0px 0px,0px 0px,0px 0px)  
### CSS : { position: absolute; top: -9999px; left: -9999px; }      <--- Some absurd position which wont be visible to the user

### CSS : There are more ways :/
### JS  : Hold my semicolon(;)

## HTML : input type='hidden' 
## HTML : hidden <-- attribute

## Bootstrap : class='hidden'



class Website_CSS_Changer:
    def __init__(self,inputHTMLPath=''):
        self.targetHTML=open(inputHTMLPath,'r').read()
        