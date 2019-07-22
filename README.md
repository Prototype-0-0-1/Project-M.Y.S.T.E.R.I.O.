----- README START -----


##--> Project M.Y.S.T.E.R.I.O.

##--> May Your Survillence Time End : Reconfigure , Invent , Outmaneuver

This is a collection of scripts which will do the following things :
    
    #1  -> Verification of the legitimacy of the website ( Prevent phishing attacks )
    
    #2  -> Staying Anonymous
            ---> Preventing / Breaking the methods of survillence
    
    #3  -> Not being vulnerable


Steps to create an Anti-Survillence Program


#_1  Anti-Phishing

##--->This module will detect whether the website you have visited is a phishing website or is the website safe ?

##--->This module is made with the assumption that the actual company websites or the companies themselves are not compromised
 
    #_1.0  Prevent the hidden auto-filling of sensitive information ( Like Email Address, Card Numbers [Credit Card,etc], Mobile Numbers )
 
    #_1.1  OSNIT investigation
 
    #_1.2  Database of all domains of the website       <-- This will be created gradually as the progarm goes on and new websites are hosted  -->
             ---->If the  website is not in the database , 
                    We scan that domain and the webpage to verify whether the website is good to go and add to the database
   
    #_1.3  Implementing a comparison method : CompareWebpage
                    ----> It will do the following steps :        <-- Light Scan -->
                        --> Compare the 'target webpage' to the 'actual webpage' hosted by the company
                        --> Detect if there is any unusual/extra information taken by the 'target webpage'
     
        #_1.4  Implementing a method : DeepScanWebpage
                    ----> It will do the following steps :      <-- Deep Scan -->
                        --> Scan the 'target webpage' 
                        --> Pass in redundant information
                        --> Get the post request
                        --> Analyze the post request to see where does the information actually go AND what all information is being sent
        
            #_1.5  Implementing a method : LeaveItToOfficials
                    ----> It will do the following steps :
                        --> Report the domains ( and if possible a DeviceScanWebpage of the device hosting the 'target website' as well ) to the actual website hosting company , the preferably all ISPs and all website hosting companies

#_2  TOR with VPN

#_3  Noisy => Redundant requests with your own request

#_4  Webcam shutdown OR Just send random images instead of the webcam output

#_5  All kind of audio input shutdown OR Just send random audio

#_6  GPS Location Change periodically

#_7  MAC adddress change periodically

#_8  Deep Scan for any backdoor on the device

#####   These are extreme level cases :   #####
##--> Manipulating your typing / keystrokes ( so that not they can't track you via your typing patterns )
##--> Manipulating the way you use the mouse ( same reason )
##--> Manipulating the networks your device connects to
##--> Manipulate your digital footprint ( Needs written conformation with signature or logo )


----- README END -----
