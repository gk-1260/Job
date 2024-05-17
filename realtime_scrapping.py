def scrapping_profiles(no_of_postings=20,table_name='sample'):#can write table_name='test' to test as test database
    from selenium import webdriver
    from bs4 import BeautifulSoup
    import time
    import pandas as pd
    import random
    from matplotlib import pyplot as plt
    import numpy as np
    #completely fine code
    data={'Title':[],'Company':[],'Role':[],'Industry_Type':[],'Department':[],'Role_Category':[],'Experience':[],'Benefits':[],'Location':[],'Skills':[],'URL':[],'Job_Description':[]}

    def each_page(n,string,no_of_postings):
        #url = "https://www.naukri.com/engineering-jobs"#"https://www.naukri.com/engineering-jobs-param"
        url=string
        if(n>1):
            url=url+"-"+str(n)
            print(url)
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(4)
        soups = BeautifulSoup(driver.page_source,'html5lib')
        soups.prettify()
        driver.close()
        #print(soup)
        results = soups.find(class_='styles_jlc__main__VdwtF')
        results.prettify()

        job_elems = results.find_all(class_='title')
        c=0 #this is count of no of profiles scraped successfully from current page
        for job_elem in job_elems:
            if(c<no_of_postings):
                url_indiv = job_elem.get("href")
                if(url_indiv==None):
                    continue
                driver = webdriver.Chrome()
                driver.get(url_indiv)
                time.sleep(0.5)
                soup = BeautifulSoup(driver.page_source,'html5lib')
                soup.prettify()
                driver.close()
                try:
                    try:
                        l=list()
                        for i in range(0,20):
                            l.append('None')
                        title_name=soup.find(class_='styles_jd-header-title__rZwM1')
                        l[0]=title_name.get_text()
                        company=soup.find(class_="styles_jd-header-comp-name__MvqAI").find('a')
                        l[1]=company.get_text()
                        elements=soup.find_all(class_='styles_details__Y424J')
                        l[2]=elements[0].get_text().split(': ')[1]#role
                        l[3]=elements[1].get_text().split(': ')[1]#industry type
                        l[4]=elements[2].get_text().split(': ')[1]#department
                        l[5]=elements[4].get_text().split(': ')[1]#role category

                        exp=soup.find(class_="styles_jhc__exp__k_giM").get_text()
                        exp=exp.split('y')[0].replace(" ","")
                        l[6]=exp#exxperience
                        
                        ben_set=soup.find_all(class_="styles_pbc__benefit__OLgb0")
                        bens=""
                        for b in ben_set:
                            bens=bens+','+b.get_text()

                        l[7]=bens.lstrip(',')#benefits
                        
                        locn=soup.find(class_="styles_jhc__location__W_pVs")
                        l[8]=locn.get_text()#location
                        
                        skills_set=soup.find_all(class_="styles_chip__7YCfG styles_clickable__dUW8S")
                        skills=""
                        for skill in skills_set:
                            skills=skills+','+skill.get_text()
                        l[9]=skills.lstrip(',')#skills
                        
                        l[10]=url_indiv#url for job posting
                        
                        desc_set=soup.find_all(class_="styles_JDC__dang-inner-html__h0K4t")
                        desc=""
                        for d in desc_set:
                            desc=desc+' '+d.get_text()
                        l[11]=desc.lstrip(',')#job description
                        
                    except:
                        continue
                    data['Title'].append(l[0])
                    data['Company'].append(l[1])
                    data['Role'].append(l[2])
                    data['Industry_Type'].append(l[3])
                    data['Department'].append(l[4])
                    data['Role_Category'].append(l[5])
                    data['Experience'].append(l[6])
                    data['Benefits'].append(l[7])
                    data['Location'].append(l[8])
                    data['Skills'].append(l[9])
                    data['URL'].append(l[10])
                    data['Job_Description'].append(l[11])
                    
                except:
                    continue
                print("x")
                
                c+=1  

                #break    #this is to scrap only 1 job profile
            else:
                break
        return c
            
    links=["https://www.naukri.com/engineering-jobs","https://www.naukri.com/data-science-jobs","https://www.naukri.com/hr-jobs","https://www.naukri.com/sales-jobs","https://www.naukri.com/finance-jobs"]
    link="https://www.naukri.com/sales-jobs"
    #"https://www.naukri.com/engineering-jobs" 
    #"https://www.naukri.com/data-science-jobs"
    #"https://www.naukri.com/finance-jobs" (1,15)
    #"https://www.naukri.com/hr-jobs" (1,25)
    #"https://www.naukri.com/sales-jobs" (1,25)
    random_link = random.choice(links)
    profiles_scraped=0
    j=0
    while(profiles_scraped>=0 and profiles_scraped<no_of_postings):
        if(profiles_scraped>=no_of_postings or profiles_scraped>30):# this is to ensure not more than few postings are scrapped at a time if program activated beacause of mistake
            break
        else:
            j+=1
            counts=each_page(j,random_link,no_of_postings-profiles_scraped)
            profiles_scraped+=counts
            print(profiles_scraped,"profiles scraped after page ",j)
    df=pd.DataFrame.from_dict(data)


    from sqlalchemy import create_engine
    import pandas as pd
    import sqlalchemy
    engine = sqlalchemy.create_engine('sqlite:///data/example.db', echo=False)
    columnList=['Title','Company','Role','Industry_Type','Department','Role_Category','Experience','Benefits','Location','Skills','URL','Job_Description']
    df.to_sql(table_name, con=engine, if_exists='append',index=False)
    print('done')


no_of_postings=2
scrapping_profiles(no_of_postings)
#no_of_postings=20 #for getting all postings in a page