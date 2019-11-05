--- Readme For AntiPhish Module Start ---


####  Anti-Phishing module
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

##--->For emails : A map [ company_web ] of ( company --> services / support  / any service that givves password-reset option / any service that makes you login )
                #   If email has been sent by anyone / any service which is not on the [ company_web ] , then the authorities will be instantly informed
                #   The authorities can henceforth check if they sent the email
                #   If the authorities didn't send the email , the email-id must be blacklisted by the mail service to avoid further phishing
                #   It will be blacklisted by this program and will give a pop-up that the email is suspicious

--- Readme For AntiPhish Module End ---