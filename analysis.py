import sqlite3 as sqlite
import pandas as pd
import plotly.graph_objects as px 


def clean_dataset(df:pd.DataFrame):
    #cleaning
    df=df.drop_duplicates(subset='URL')
    df[['Min_Exp','Max_Exp']] = df.Experience.apply(lambda x: pd.Series(str(x).split("-")))
    df['Role']=df['Role'].str.rstrip(',')
    df['Industry_Type']=df['Industry_Type'].str.rstrip(',')
    df['Department']=df['Department'].str.rstrip(',')
    df=df.drop(['Benefits'], axis=1)
    df=df.apply(lambda x: x.astype(str).str.lower())
    df = df.replace(['nofixedduration'], '0')
    return df

def analyse_and_visualize(df:pd.DataFrame,sample_colors:list):
    # DSML ********************************************************************************************************************
    dsmldf=df.loc[df['Role_Category'] == "data science & machine learning"]

    df2=pd.DataFrame(dsmldf.Min_Exp.apply(pd.Series).stack().value_counts()[:10]).reset_index()
    df2.columns=["Min_Exp","count"]
    random_x=list(df2["Min_Exp"])
    random_y=list(df2["count"])
    plot = px.Figure(data=[px.Line( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="DSML Minimum Experience Required"
                        ,x=0.5),xaxis_title="Min Years of Experience",yaxis_title="Jobs"))
    #Add dropdown 
    plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    ),
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ),
                ]), 
                direction="down", 
            ), 
        ] 
    ) 
    #plot.show()
    plot.write_html(r"templates\charts\dsml_c1.html",full_html=False,include_plotlyjs='cdn')

    jjdsml=pd.DataFrame(dsmldf.Skills.apply(pd.Series).stack().value_counts()).reset_index()
    jjdsml.columns=["skills","count"]
    datascience={}
    datascience['statistics']=jjdsml["count"][jjdsml['skills'].str.contains('stat', regex=True)].sum()
    datascience['machine_learning']=jjdsml["count"][jjdsml['skills'].str.contains('machine |^ml|ML', regex=True)].sum()
    datascience['data_analysis']=jjdsml["count"][jjdsml['skills'].str.contains('data ana', regex=True)].sum()
    datascience['data_mining']=jjdsml["count"][jjdsml['skills'].str.contains('mining', regex=True)].sum()
    datascience['nlp']=jjdsml["count"][jjdsml['skills'].str.contains('NLP|Natural|nlp|natural', regex=True)].sum()
    datascience['deep_learning']=jjdsml["count"][jjdsml['skills'].str.contains('Deep learning|deep learning', regex=True)].sum()
    datascience['big_data']=jjdsml["count"][jjdsml['skills'].str.contains('Big|big', regex=True)].sum()
    datascience['Artificial Intelligence']=jjdsml["count"][jjdsml['skills'].str.contains('Artificial|artificial', regex=True)].sum()
    from operator import itemgetter
    datascience=dict(sorted(datascience.items(), key=itemgetter(1),reverse=True))

    random_x=list(datascience.keys())
    random_y=list(datascience.values())
    plot = px.Figure(data=[px.Pie(labels=random_x,values=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Skills for DSML"
                        ,x=0.5),xaxis_title="Skills",yaxis_title="Jobs"))
    #plot.update_traces(marker_color=sample_colors)
    #plot.update_traces(marker=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ), 
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    )
                ]), 
                direction="down", 
            ), 
        ] 
    )
    #plot.update_traces(marker_color=sample_colors)
    #plot.show()
    plot.write_html(r"templates\charts\dsml_c2.html",full_html=False,include_plotlyjs='cdn')

    jjdsmlloc=pd.DataFrame(dsmldf.Location.apply(pd.Series).stack().value_counts()).reset_index()
    jjdsmlloc.columns=["locations","count"]
    dsmllocations={}
    dsmllocations["noida"]=jjdsmlloc["count"][jjdsmlloc['locations'].str.contains('noida', regex=True)].sum()
    dsmllocations["bangalore"]=jjdsmlloc["count"][jjdsmlloc['locations'].str.contains('bangalore|bengaluru', regex=True)].sum()
    dsmllocations["chennai"]=jjdsmlloc["count"][jjdsmlloc['locations'].str.contains('chennai', regex=True)].sum()
    dsmllocations["remote"]=jjdsmlloc["count"][jjdsmlloc['locations'].str.contains('remote', regex=True)].sum()
    dsmllocations["gurugram"]=jjdsmlloc["count"][jjdsmlloc['locations'].str.contains('gurgoan|gurugram', regex=True)].sum()
    dsmllocations["mumbai"]=jjdsmlloc["count"][jjdsmlloc['locations'].str.contains('mumbai', regex=True)].sum()
    dsmllocations["pune"]=jjdsmlloc["count"][jjdsmlloc['locations'].str.contains('pune', regex=True)].sum()
    dsmllocations["hyderabad"]=jjdsmlloc["count"][jjdsmlloc['locations'].str.contains('hyderabad', regex=True)].sum()
    dsmllocations["delhi"]=jjdsmlloc["count"][jjdsmlloc['locations'].str.contains('new delhi', regex=True)].sum()
    dsmllocations["kolkata"]=jjdsmlloc["count"][jjdsmlloc['locations'].str.contains('kolkata', regex=True)].sum()
    dsmllocations["chandigarh"]=jjdsmlloc["count"][jjdsmlloc['locations'].str.contains('chandigarh', regex=True)].sum()
    from operator import itemgetter
    dsmllocations=dict(sorted(dsmllocations.items(), key=itemgetter(1),reverse=True))

    random_x=list(dsmllocations.keys())
    random_y=list(dsmllocations.values())
    plot = px.Figure(data=[px.Bar( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="DSML Locations"
                        ,x=0.5),xaxis_title="Locations",yaxis_title="Jobs"))
    plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ), 
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    )
                ]), 
                direction="down", 
            ), 
        ] 
    ) 
    #plot.show()
    plot.write_html(r"templates\charts\dsml_c3.html",full_html=False,include_plotlyjs='cdn')



    languages={}
    languages["python"]=jjdsml["count"][jjdsml['skills'].str.contains('Python|python', regex=True)].sum()
    languages["c++"]=jjdsml["count"][jjdsml['skills'].str.contains('C\++|c\++', regex=True)].sum()
    languages["git"]=jjdsml["count"][jjdsml['skills'].str.contains('Git|git', regex=True)].sum()
    languages["javascript"]=jjdsml["count"][jjdsml['skills'].str.contains('Javascript|javascript', regex=True)].sum()
    #to identify the Sql first and then seperate the nosql from the list
    sql=jjdsml[jjdsml['skills'].str.contains('sql', regex=True)]
    languages["sql"]=sql["count"][~sql['skills'].str.contains('no', regex=True)].sum()

    #to sort the dictionary
    languages=dict(sorted(languages.items(), key=itemgetter(1),reverse=True))
    #plt.bar(languages.keys(),languages.values(),color=["r","b","y","pink","m"])
    #plt.xticks(rotation=45,fontsize=15)
    #plt.title("Programming languages for Data science",fontsize=18)
    #plt.show()
    random_x=list(languages.keys())
    random_y=list(languages.values())
    plot = px.Figure(data=[px.Bar( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Languages required for DSML"
                        ,x=0.5),xaxis_title="Languages",yaxis_title="Jobs"))
    plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ), 
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    )
                ]), 
                direction="down", 
            ), 
        ] 
    ) 
    #plot.show()
    plot.write_html(r"templates\charts\dsml_c4.html",full_html=False,include_plotlyjs='cdn')


    # ENGINEERING ********************************************************************************************************************

    engdf=df.loc[df['Role_Category'] == "engineering"]
    engdf["Min_Exp"].value_counts()[:10].plot.barh(figsize=(8,5),fontsize=13,color="b")
    df2=pd.DataFrame(engdf.Min_Exp.apply(pd.Series).stack().value_counts()[:10]).reset_index()
    df2.columns=["Min_Exp","count"]
    random_x=list(df2["Min_Exp"])
    random_y=list(df2["count"])
    plot = px.Figure(data=[px.Line( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Engineering Minimum Experience Required"
                        ,x=0.5),xaxis_title="Min Years of Experience",yaxis_title="Jobs"))
    #Add dropdown 
    plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    ),
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ),
                ]), 
                direction="down", 
            ), 
        ] 
    )
    #plot.show()
    plot.write_html(r"templates\charts\engineering_c1.html",full_html=False,include_plotlyjs='cdn')



    engdf=df.loc[df['Role_Category'] == "engineering"]
    engdf.Role.apply(pd.Series).stack().value_counts()[:32].plot(kind="bar",figsize=(18,6),fontsize=15)
    df2=pd.DataFrame(engdf.Role.apply(pd.Series).stack().value_counts()[:10]).reset_index()
    df2.columns=["Role","count"]
    random_x=list(df2["Role"])
    random_y=list(df2["count"])
    plot = px.Figure(data=[px.Pie(labels=random_x,values=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Types of Engineering Roles"
                        ,x=0.5),xaxis_title="Roles",yaxis_title="Jobs"))
    #Add dropdown 
    #plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ), 
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    )
                ]), 
                direction="down", 
            ), 
        ] 
    ) 
    #plot.show()
    plot.write_html(r"templates\charts\engineering_c2.html",full_html=False,include_plotlyjs='cdn')



    jjengloc=pd.DataFrame(engdf.Location.apply(pd.Series).stack().value_counts()).reset_index()
    jjengloc.columns=["locations","count"]
    englocations={}
    englocations["noida"]=jjengloc["count"][jjengloc['locations'].str.contains('noida', regex=True)].sum()
    englocations["bangalore"]=jjengloc["count"][jjengloc['locations'].str.contains('bangalore|bengaluru', regex=True)].sum()
    englocations["chennai"]=jjengloc["count"][jjengloc['locations'].str.contains('chennai', regex=True)].sum()
    englocations["remote"]=jjengloc["count"][jjengloc['locations'].str.contains('remote', regex=True)].sum()
    englocations["gurugram"]=jjengloc["count"][jjengloc['locations'].str.contains('gurgoan|gurugram', regex=True)].sum()
    englocations["mumbai"]=jjengloc["count"][jjengloc['locations'].str.contains('mumbai', regex=True)].sum()
    englocations["pune"]=jjengloc["count"][jjengloc['locations'].str.contains('pune', regex=True)].sum()
    englocations["hyderabad"]=jjengloc["count"][jjengloc['locations'].str.contains('hyderabad', regex=True)].sum()
    englocations["delhi"]=jjengloc["count"][jjengloc['locations'].str.contains('new delhi|delhi', regex=True)].sum()
    englocations["kolkata"]=jjengloc["count"][jjengloc['locations'].str.contains('kolkata', regex=True)].sum()
    englocations["chandigarh"]=jjengloc["count"][jjengloc['locations'].str.contains('chandigarh', regex=True)].sum()
    from operator import itemgetter
    englocations=dict(sorted(englocations.items(), key=itemgetter(1),reverse=True))
    random_x=list(englocations.keys())
    random_y=list(englocations.values())
    plot = px.Figure(data=[px.Bar( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Engineering Locations"
                        ,x=0.5),xaxis_title="Locations",yaxis_title="Jobs"))
    plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ), 
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    )
                ]), 
                direction="down", 
            ), 
        ] 
    ) 
    #plot.show()
    plot.write_html(r"templates\charts\engineering_c3.html",full_html=False,include_plotlyjs='cdn')



    # HR ********************************************************************************************************************

    hrdf=df.loc[df['Role_Category'] == "hr operations"]
    hrdf["Min_Exp"].value_counts()[:10].plot.barh(figsize=(8,5),fontsize=13,color="b")
    df2=pd.DataFrame(hrdf.Min_Exp.apply(pd.Series).stack().value_counts()[:10]).reset_index()
    df2.columns=["Min_Exp","count"]
    random_x=list(df2["Min_Exp"])
    random_y=list(df2["count"])
    plot = px.Figure(data=[px.Line( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="HR Minimum Experience Required"
                        ,x=0.5),xaxis_title="Min Years of Experience",yaxis_title="Jobs"))
    #Add dropdown 
    plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    ),
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ),
                ]), 
                direction="down", 
            ), 
        ] 
    ) 
    #plot.show()
    plot.write_html(r"templates\charts\hr_c1.html",full_html=False,include_plotlyjs='cdn')


    jjhr=pd.DataFrame(hrdf.Skills.apply(pd.Series).stack().value_counts()).reset_index()
    jjhr.columns=["skills","count"]
    hr={}
    hr['communication']=jjhr["count"][jjhr['skills'].str.contains('communication', regex=True)].sum()
    hr['training']=jjhr["count"][jjhr['skills'].str.contains('training|Training', regex=True)].sum()
    hr['talent aquision']=jjhr["count"][jjhr['skills'].str.contains('Talent|talent', regex=True)].sum()
    hr['recruiter']=jjhr["count"][jjhr['skills'].str.contains('Recruiter|recruiter|recruitment', regex=True)].sum()
    hr['management']=jjhr["count"][jjhr['skills'].str.contains('management', regex=True)].sum()
    hr['BBA']=jjhr["count"][jjhr['skills'].str.contains('BBA|bba', regex=True)].sum()
    hr['administration']=jjhr["count"][jjhr['skills'].str.contains('Administration|admin', regex=True)].sum()
    hr['operations']=jjhr["count"][jjhr['skills'].str.contains('operation', regex=True)].sum()
    from operator import itemgetter
    hr=dict(sorted(hr.items(), key=itemgetter(1),reverse=True))
    random_x=list(hr.keys())
    random_y=list(hr.values())
    plot = px.Figure(data=[px.Pie(labels=random_x,values=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="HR Must Have Skills"
                        ,x=0.5),xaxis_title="HR Skills",yaxis_title="Jobs"))
    #plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ), 
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    )
                ]), 
                direction="down", 
            ), 
        ] 
    )
    #plot.show()
    plot.write_html(r"templates\charts\hr_c2.html",full_html=False,include_plotlyjs='cdn')


    jjhrloc=pd.DataFrame(hrdf.Location.apply(pd.Series).stack().value_counts()).reset_index()
    jjhrloc.columns=["locations","count"]
    hrlocations={}
    hrlocations["noida"]=jjhrloc["count"][jjhrloc['locations'].str.contains('noida', regex=True)].sum()
    hrlocations["bangalore"]=jjhrloc["count"][jjhrloc['locations'].str.contains('bangalore|bengaluru', regex=True)].sum()
    hrlocations["chennai"]=jjhrloc["count"][jjhrloc['locations'].str.contains('chennai', regex=True)].sum()
    hrlocations["remote"]=jjhrloc["count"][jjhrloc['locations'].str.contains('remote', regex=True)].sum()
    hrlocations["gurugram"]=jjhrloc["count"][jjhrloc['locations'].str.contains('gurgoan|gurugram', regex=True)].sum()
    hrlocations["mumbai"]=jjhrloc["count"][jjhrloc['locations'].str.contains('mumbai', regex=True)].sum()
    hrlocations["pune"]=jjhrloc["count"][jjhrloc['locations'].str.contains('pune', regex=True)].sum()
    hrlocations["hyderabad"]=jjhrloc["count"][jjhrloc['locations'].str.contains('hyderabad', regex=True)].sum()
    hrlocations["delhi"]=jjhrloc["count"][jjhrloc['locations'].str.contains('new delhi|delhi', regex=True)].sum()
    hrlocations["kolkata"]=jjhrloc["count"][jjhrloc['locations'].str.contains('kolkata', regex=True)].sum()
    hrlocations["chandigarh"]=jjhrloc["count"][jjhrloc['locations'].str.contains('chandigarh', regex=True)].sum()
    from operator import itemgetter
    hrlocations=dict(sorted(hrlocations.items(), key=itemgetter(1),reverse=True))
    random_x=list(hrlocations.keys())
    random_y=list(hrlocations.values())
    plot = px.Figure(data=[px.Bar( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="HR Locations"
                        ,x=0.5),xaxis_title="HR Locations",yaxis_title="Jobs"))
    plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ), 
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    )
                ]), 
                direction="down", 
            ), 
        ] 
    ) 
    #plot.show()
    plot.write_html(r"templates\charts\hr_c3.html",full_html=False,include_plotlyjs='cdn')
    
    # SUPPORT ********************************************************************************************************************
    # orientation='h'
    supportdf=df.loc[(df['Role_Category']=='operations, maintenance & support')|(df['Role_Category']=='sales support & operations')|(df['Role_Category']=='surveying ')]

    supportdf["Min_Exp"].value_counts()[:10].plot.barh(figsize=(8,5),fontsize=13,color="b")
    #plt.xlabel("No.of Vacancies",fontsize=18)
    #plt.ylabel("Minimum Experience",fontsize=18)
    #plt.show()

    df2=pd.DataFrame(supportdf.Min_Exp.apply(pd.Series).stack().value_counts()[:10]).reset_index()
    df2.columns=["Min_Exp","count"]
    random_x=list(df2["Min_Exp"])
    random_y=list(df2["count"])
    plot = px.Figure(data=[px.Line( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Support Minimum Experience Required"
                        ,x=0.5),xaxis_title="Min Years of Experience",yaxis_title="Jobs"))
    #Add dropdown 
    plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    ),
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ),
                ]), 
                direction="down", 
            ), 
        ] 
    ) 
    #plot.show()
    plot.write_html(r"templates\charts\support_c1.html",full_html=False,include_plotlyjs='cdn')



    jjsupport=pd.DataFrame(supportdf.Skills.apply(pd.Series).stack().value_counts()).reset_index()
    jjsupport.columns=["skills","count"]
    sup={}
    #maintainance troubleshooting communication-skills supervise management operations
    sup['maintainance']=jjsupport["count"][jjsupport['skills'].str.contains('maintainance|maintenance|maintain|mainten', regex=True)].sum()
    sup['troubleshooting']=jjsupport["count"][jjsupport['skills'].str.contains('troubleshooting', regex=True)].sum()
    sup['communication']=jjsupport["count"][jjsupport['skills'].str.contains('communication|interpersonal|relationship|acquisition', regex=True)].sum()
    sup['supervising']=jjsupport["count"][jjsupport['skills'].str.contains('supervis|train', regex=True)].sum()
    sup['management']=jjsupport["count"][jjsupport['skills'].str.contains('management|strategy|plan|analy', regex=True)].sum()
    sup['operations']=jjsupport["count"][jjsupport['skills'].str.contains('operation', regex=True)].sum()
    sup['sales']=jjsupport["count"][jjsupport['skills'].str.contains('sales|corporate|sell', regex=True)].sum()
    sup['technical']=jjsupport["count"][jjsupport['skills'].str.contains('technical|system|software|heavy|engine|tool|production|electric|mechan}automat', regex=True)].sum()

    from operator import itemgetter
    sup=dict(sorted(sup.items(), key=itemgetter(1),reverse=True))


    random_x=list(sup.keys())
    random_y=list(sup.values())
    plot = px.Figure(data=[px.Pie(labels=random_x,values=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Support Must Have Skills"
                        ,x=0.5),xaxis_title="Different Skills",yaxis_title="Jobs"))
    #plot.update_layout(title_text="Support Skills",title_x=0.5)
    #plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ), 
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    )
                ]), 
                direction="down", 
            ), 
        ] 
    )
    #plot.show()
    plot.write_html(r"templates\charts\support_c2.html",full_html=False,include_plotlyjs='cdn')


    jjsuploc=pd.DataFrame(supportdf.Location.apply(pd.Series).stack().value_counts()).reset_index()
    jjsuploc.columns=["locations","count"]
    jjsuploc

    suplocations={}
    suplocations["noida"]=jjsuploc["count"][jjsuploc['locations'].str.contains('Noida|noida', regex=True)].sum()
    suplocations["bangalore"]=jjsuploc["count"][jjsuploc['locations'].str.contains('Bangalore|Bengaluru|bangalore|bengaluru', regex=True)].sum()
    suplocations["chennai"]=jjsuploc["count"][jjsuploc['locations'].str.contains('Chennai|chennai', regex=True)].sum()
    suplocations["cochin"]=jjsuploc["count"][jjsuploc['locations'].str.contains('cochin|kochi', regex=True)].sum()
    suplocations["gurugram"]=jjsuploc["count"][jjsuploc['locations'].str.contains('Gurgoan|Gurugram|gurgoan|gurugram|faridabad', regex=True)].sum()
    suplocations["mumbai"]=jjsuploc["count"][jjsuploc['locations'].str.contains('Mumbai|mumbai', regex=True)].sum()
    suplocations["pune"]=jjsuploc["count"][jjsuploc['locations'].str.contains('Pune|pune', regex=True)].sum()
    suplocations["hyderabad"]=jjsuploc["count"][jjsuploc['locations'].str.contains('Hyderabad|hyderabad', regex=True)].sum()
    suplocations["delhi"]=jjsuploc["count"][jjsuploc['locations'].str.contains('New Delhi|delhi|ncr', regex=True)].sum()
    suplocations["kolkata"]=jjsuploc["count"][jjsuploc['locations'].str.contains('Kolkata|kolkata', regex=True)].sum()
    suplocations["chandigarh"]=jjsuploc["count"][jjsuploc['locations'].str.contains('Chandigarh|chandigarh', regex=True)].sum()
    from operator import itemgetter
    suplocations=dict(sorted(suplocations.items(), key=itemgetter(1),reverse=True))

    random_x=list(suplocations.keys())
    random_y=list(suplocations.values())
    plot = px.Figure(data=[px.Bar( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Support Locations"
                        ,x=0.5),xaxis_title="Different Locations",yaxis_title="Jobs") )
    plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ), 
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    )
                ]), 
                direction="down", 
            ), 
        ] 
    ) 
    #plot.show()
    plot.write_html(r"templates\charts\support_c3.html",full_html=False,include_plotlyjs='cdn')



    # FINANCE ********************************************************************************************************************

    financedf=df.loc[(df['Role_Category']=='finance')|(df['Role_Category']=='finance & accounting - other')|(df['Role_Category']=='accounting & taxation')|(df['Role_Category']=='treasury ')]

    df2=pd.DataFrame(financedf.Min_Exp.apply(pd.Series).stack().value_counts()[:10]).reset_index()
    df2.columns=["Min_Exp","count"]
    random_x=list(df2["Min_Exp"])
    random_y=list(df2["count"])
    plot = px.Figure(data=[px.Line( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Finance Minimum Experience Required"
                        ,x=0.5),xaxis_title="Min Years of Experience",yaxis_title="Jobs"))
    #Add dropdown 
    plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    ),
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ),
                ]), 
                direction="down", 
            ), 
        ] 
    ) 
    #plot.show()
    plot.write_html(r"templates\charts\finance_c1.html",full_html=False,include_plotlyjs='cdn')


    jjfin=pd.DataFrame(financedf.Skills.apply(pd.Series).stack().value_counts()).reset_index()
    jjfin.columns=["skills","count"]
    fin={}
    #planning/strategy/management accounting auditing communication taxation reporting budgeting reconcilation analysis/processing 
    fin['management']=jjfin["count"][jjfin['skills'].str.contains('management|strategy|plan|manage', regex=True)].sum()
    fin['accounting']=jjfin["count"][jjfin['skills'].str.contains('accounting|account|gst|finance', regex=True)].sum()
    fin['auditing']=jjfin["count"][jjfin['skills'].str.contains('auditing|audit', regex=True)].sum()
    fin['communication']=jjfin["count"][jjfin['skills'].str.contains('communication|interpersonal|relationship|acquisition', regex=True)].sum()
    fin['taxation']=jjfin["count"][jjfin['skills'].str.contains('tax', regex=True)].sum()
    fin['reporting']=jjfin["count"][jjfin['skills'].str.contains('reporting|report', regex=True)].sum()
    fin['budgeting']=jjfin["count"][jjfin['skills'].str.contains('budgeting|budget', regex=True)].sum()
    fin['reconcilation']=jjfin["count"][jjfin['skills'].str.contains('reconcilation|reconcile|reconcil|consolidat', regex=True)].sum()
    fin['analysis']=jjfin["count"][jjfin['skills'].str.contains('analysis|processing|analys|process|research', regex=True)].sum()

    from operator import itemgetter
    fin=dict(sorted(fin.items(), key=itemgetter(1),reverse=True))

    random_x=list(fin.keys())
    random_y=list(fin.values())
    plot = px.Figure(data=[px.Pie(labels=random_x,values=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Finance Must Have Skills"
                        ,x=0.5),xaxis_title="Different Skills",yaxis_title="Jobs"))
    #plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ), 
                    dict( 
                        args=["type", "bar"], 
                        label="Horizontal Bar Chart", 
                        method="restyle"
                    ),
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    )
                ]), 
                direction="down", 
            ), 
        ] 
    ) 
    #plot.show()
    plot.write_html(r"templates\charts\finance_c2.html",full_html=False,include_plotlyjs='cdn')


    jjfinloc=pd.DataFrame(financedf.Location.apply(pd.Series).stack().value_counts()).reset_index()
    jjfinloc.columns=["locations","count"]

    finlocations={}
    finlocations["noida"]=jjfinloc["count"][jjfinloc['locations'].str.contains('Noida|noida|ghaziabad', regex=True)].sum()
    finlocations["bangalore"]=jjfinloc["count"][jjfinloc['locations'].str.contains('Bangalore|Bengaluru|bangalore|bengaluru', regex=True)].sum()
    finlocations["chennai"]=jjfinloc["count"][jjfinloc['locations'].str.contains('Chennai|chennai', regex=True)].sum()
    finlocations["ahmedabad"]=jjfinloc["count"][jjfinloc['locations'].str.contains('ahmedabad|vadodara', regex=True)].sum()
    finlocations["gurugram"]=jjfinloc["count"][jjfinloc['locations'].str.contains('Gurgoan|Gurugram|gurgoan|gurugram|faridabad', regex=True)].sum()
    finlocations["mumbai"]=jjfinloc["count"][jjfinloc['locations'].str.contains('Mumbai|mumbai', regex=True)].sum()
    finlocations["pune"]=jjfinloc["count"][jjfinloc['locations'].str.contains('Pune|pune', regex=True)].sum()
    finlocations["hyderabad"]=jjfinloc["count"][jjfinloc['locations'].str.contains('Hyderabad|hyderabad', regex=True)].sum()
    finlocations["delhi"]=jjfinloc["count"][jjfinloc['locations'].str.contains('New Delhi|delhi|ncr', regex=True)].sum()
    finlocations["kolkata"]=jjfinloc["count"][jjfinloc['locations'].str.contains('Kolkata|kolkata', regex=True)].sum()
    finlocations["amritsar"]=jjfinloc["count"][jjfinloc['locations'].str.contains('Amritsar|amritsar', regex=True)].sum()
    from operator import itemgetter
    finlocations=dict(sorted(finlocations.items(), key=itemgetter(1),reverse=True))

    random_x=list(finlocations.keys())
    random_y=list(finlocations.values())
    plot = px.Figure(data=[px.Bar( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Finance Locations"
                        ,x=0.5),xaxis_title="Different Locations",yaxis_title="Jobs") )
    plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ), 
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    )
                ]), 
                direction="down", 
            ), 
        ] 
    )  
    #plot.show()
    plot.write_html(r"templates\charts\finance_c3.html",full_html=False,include_plotlyjs='cdn')


    # BIA ********************************************************************************************************************

    biadf=df.loc[(df['Role_Category']=='business intelligence & analytics')]


    df2=pd.DataFrame(biadf.Min_Exp.apply(pd.Series).stack().value_counts()[:10]).reset_index()
    df2.columns=["Min_Exp","count"]
    random_x=list(df2["Min_Exp"])
    random_y=list(df2["count"])
    plot = px.Figure(data=[px.Line( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Business Intelligence & Analytics Minimum Experience Required"
                        ,x=0.5),xaxis_title="Min Years of Experience",yaxis_title="Jobs"))
    #Add dropdown 
    plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    ),
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ),
                ]), 
                direction="down", 
            ), 
        ] 
    ) 
    #plot.show()
    plot.write_html(r"templates\charts\bia_c1.html",full_html=False,include_plotlyjs='cdn')




    jjbia=pd.DataFrame(biadf.Skills.apply(pd.Series).stack().value_counts()).reset_index()
    jjbia.columns=["skills","count"]
    bia={}
    #management/planning python sql data-science IT financing consulting/reporting  analysis
    bia['management']=jjbia["count"][jjbia['skills'].str.contains('management|strategy|plan|manag', regex=True)].sum()
    bia['python']=jjbia["count"][jjbia['skills'].str.contains('python', regex=True)].sum()
    bia['sql']=jjbia["count"][jjbia['skills'].str.contains('sql|structure|query|oracle|open source', regex=True)].sum()
    bia['data science']=jjbia["count"][jjbia['skills'].str.contains('data|science|machine learning|learning|artificial intelligence|nueral network|hadoop', regex=True)].sum()
    bia['IT']=jjbia["count"][jjbia['skills'].str.contains('IT|logistic|java|perl|git|digital|simul|it|apache|excel|cloud|agile|progamming|sas|sap|automotive', regex=True)].sum()
    bia['financing']=jjbia["count"][jjbia['skills'].str.contains('sale|finance|financ|sell|business|commerce|com', regex=True)].sum()
    bia['consulting']=jjbia["count"][jjbia['skills'].str.contains('consulting|reporting|relationship|consult|report|hr', regex=True)].sum()
    bia['analysing']=jjbia["count"][jjbia['skills'].str.contains('analysis|research|analy', regex=True)].sum()

    from operator import itemgetter
    bia=dict(sorted(bia.items(), key=itemgetter(1),reverse=True))
    random_x=list(bia.keys())
    random_y=list(bia.values())
    plot = px.Figure(data=[px.Pie(labels=random_x,values=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Business Intelligence & Analytics Must Have Skills"
                        ,x=0.5),xaxis_title="Different Skills",yaxis_title="Jobs"))
    #plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ), 
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    )
                ]), 
                direction="down", 
            ), 
        ] 
    )
    #plot.show()
    plot.write_html(r"templates\charts\bia_c2.html",full_html=False,include_plotlyjs='cdn')


    jjbialoc=pd.DataFrame(biadf.Location.apply(pd.Series).stack().value_counts()).reset_index()
    jjbialoc.columns=["locations","count"]

    bialocations={}
    bialocations["noida"]=jjbialoc["count"][jjbialoc['locations'].str.contains('Noida|noida', regex=True)].sum()
    bialocations["bangalore"]=jjbialoc["count"][jjbialoc['locations'].str.contains('Bangalore|Bengaluru|bangalore|bengaluru', regex=True)].sum()
    bialocations["chennai"]=jjbialoc["count"][jjbialoc['locations'].str.contains('Chennai|chennai', regex=True)].sum()
    bialocations["cochin"]=jjbialoc["count"][jjbialoc['locations'].str.contains('cochin|kochi', regex=True)].sum()
    bialocations["gurugram"]=jjbialoc["count"][jjbialoc['locations'].str.contains('Gurgoan|Gurugram|gurgoan|gurugram|faridabad', regex=True)].sum()
    bialocations["mumbai"]=jjbialoc["count"][jjbialoc['locations'].str.contains('Mumbai|mumbai', regex=True)].sum()
    bialocations["pune"]=jjbialoc["count"][jjbialoc['locations'].str.contains('Pune|pune', regex=True)].sum()
    bialocations["hyderabad"]=jjbialoc["count"][jjbialoc['locations'].str.contains('Hyderabad|hyderabad', regex=True)].sum()
    bialocations["delhi"]=jjbialoc["count"][jjbialoc['locations'].str.contains('New Delhi|delhi|ncr', regex=True)].sum()
    bialocations["kolkata"]=jjbialoc["count"][jjbialoc['locations'].str.contains('Kolkata|kolkata', regex=True)].sum()
    bialocations["remote"]=jjbialoc["count"][jjbialoc['locations'].str.contains('remote', regex=True)].sum()
    from operator import itemgetter
    bialocations=dict(sorted(bialocations.items(), key=itemgetter(1),reverse=True))

    random_x=list(bialocations.keys())
    random_y=list(bialocations.values())
    plot = px.Figure(data=[px.Bar( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Business Intelligence & Analytics Locations"
                        ,x=0.5),xaxis_title="Different Locations",yaxis_title="Jobs") )
    plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ), 
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    )
                ]), 
                direction="down", 
            ), 
        ] 
    ) 
    #plot.show()
    plot.write_html(r"templates\charts\bia_c3.html",full_html=False,include_plotlyjs='cdn')
    
    # MANAGEMENT ********************************************************************************************************************

    managedf=df.loc[(df['Role_Category']=='management')]

    df2=pd.DataFrame(managedf.Min_Exp.apply(pd.Series).stack().value_counts()[:10]).reset_index()
    df2.columns=["Min_Exp","count"]
    random_x=list(df2["Min_Exp"])
    random_y=list(df2["count"])
    plot = px.Figure(data=[px.Line( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Min Experience for Management"
                        ,x=0.5),xaxis_title="Min_Exp",yaxis_title="Jobs"))
    plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    ),
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ),
                ]), 
                direction="down", 
            ), 
        ] 
    ) 
    #plot.show()
    plot.write_html(r"templates\charts\management_c1.html",full_html=False,include_plotlyjs='cdn')


    jjmanage=pd.DataFrame(managedf.Skills.apply(pd.Series).stack().value_counts()).reset_index()
    jjmanage.columns=["skills","count"]
    manage={}
    manage['production']=jjmanage["count"][jjmanage['skills'].str.contains('production management|production manager|production control|production', regex=True)].sum()
    manage['management']=jjmanage["count"][jjmanage['skills'].str.contains('project management|analytical|operations|supervision|budgeting', regex=True)].sum()
    manage['mechanical']=jjmanage["count"][jjmanage['skills'].str.contains('plant operations|mechanical maintenance|sap|factory operations|procurement|electronics|packaging|renewable energy|automotive', regex=True)].sum()

    from operator import itemgetter
    manage=dict(sorted(manage.items(), key=itemgetter(1),reverse=True))

    random_x=list(manage.keys())
    random_y=list(manage.values())
    plot = px.Figure(data=[px.Pie(labels=random_x,values=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Management Skills"
                        ,x=0.5),xaxis_title="Skills",yaxis_title="Jobs"))
    #plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ), 
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    )
                ]), 
                direction="down", 
            ), 
        ] 
    ) 
    #plot.show()
    plot.write_html(r"templates\charts\management_c2.html",full_html=False,include_plotlyjs='cdn')


    jjmangloc=pd.DataFrame(managedf.Location.apply(pd.Series).stack().value_counts()).reset_index()
    jjmangloc.columns=["locations","count"]
    managelocations={}
    managelocations["noida"]=jjmangloc["count"][jjmangloc['locations'].str.contains('Noida|noida|greater noida', regex=True)].sum()
    managelocations["delhi/ncr"]=jjmangloc["count"][jjmangloc['locations'].str.contains('delhi|new delhi|delhi/ncr|rajpura', regex=True)].sum()
    managelocations["mumbai"]=jjmangloc["count"][jjmangloc['locations'].str.contains('rampur| mumbai|jamanagar', regex=True)].sum()
    managelocations["gurgaon"]=jjmangloc["count"][jjmangloc['locations'].str.contains('gurgaon|ballabhagrh|faridabad|gurugram|manesar', regex=True)].sum()
    managelocations["chennai"]=jjmangloc["count"][jjmangloc['locations'].str.contains('chennai|pune|hasur', regex=True)].sum()
    managelocations["hyderabad"]=jjmangloc["count"][jjmangloc['locations'].str.contains('hyderabad', regex=True)].sum()

    from operator import itemgetter
    managelocations=dict(sorted(managelocations.items(), key=itemgetter(1),reverse=True))

    random_x=list(managelocations.keys())
    random_y=list(managelocations.values())
    plot = px.Figure(data=[px.Bar( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Management Locations"
                        ,x=0.5),xaxis_title="Locations",yaxis_title="Jobs"))
    plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ), 
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    )
                ]), 
                direction="down", 
            ), 
        ] 
    ) 
    #plot.show()
    plot.write_html(r"templates\charts\management_c3.html",full_html=False,include_plotlyjs='cdn')


    # BANKING ********************************************************************************************************************
    bankdf=df.loc[(df['Role_Category']=='investment banking, private equity & vc')|(df['Role_Category']=='trading, asset & wealth management')|(df['Role_Category']=='banking operation')|(df['Role_Category']=='bfsi, investments & trading')]
    bankdf["Min_Exp"].value_counts()[:10].plot.barh(figsize=(8,5),fontsize=13,color="b")
    df2=pd.DataFrame(bankdf.Min_Exp.apply(pd.Series).stack().value_counts()[:10]).reset_index()
    df2.columns=["Min_Exp","count"]
    random_x=list(df2["Min_Exp"])
    random_y=list(df2["count"])
    plot = px.Figure(data=[px.Line( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Min Experience for Banking"
                        ,x=0.5),xaxis_title="Min_Exp",yaxis_title="Jobs"))
    plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    ),
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ),
                ]), 
                direction="down", 
            ), 
        ] 
    ) 
    #plot.show()
    plot.write_html(r"templates\charts\banking_c1.html",full_html=False,include_plotlyjs='cdn')


    jjbank=pd.DataFrame(bankdf.Skills.apply(pd.Series).stack().value_counts()).reset_index()
    jjbank.columns=["skills","count"]
    bank={}
    bank['bank branch management']=jjbank["count"][jjbank['skills'].str.contains('account management|financial management|accounting operations|backend operation|banking sales', regex=True)].sum()
    bank['client management']=jjbank["count"][jjbank['skills'].str.contains('client servicing|client relationship|new client acquisition|relationship management|financial advisory|marketing support', regex=True)].sum()
    bank['policies']=jjbank["count"][jjbank['skills'].str.contains('investment products|tpp|demat|third party products|financial advisory|aml|kyc|freshers', regex=True)].sum()

    from operator import itemgetter
    bank=dict(sorted(bank.items(), key=itemgetter(1),reverse=True))
    random_x=list(bank.keys())
    random_y=list(bank.values())
    plot = px.Figure(data=[px.Pie(labels=random_x,values=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Banking Skills"
                        ,x=0.5),xaxis_title="Skills",yaxis_title="Jobs"))
    #plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ), 
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    )
                ]), 
                direction="down", 
            ), 
        ] 
    ) 
    #plot.show()
    plot.write_html(r"templates\charts\banking_c2.html",full_html=False,include_plotlyjs='cdn')


    jjbankloc=pd.DataFrame(bankdf.Location.apply(pd.Series).stack().value_counts()).reset_index()
    jjbankloc.columns=["locations","count"]
    banklocations={}
    banklocations["noida"]=jjbankloc["count"][jjbankloc['locations'].str.contains('Noida|noida|ghaziabad', regex=True)].sum()
    banklocations["gurgaon"]=jjbankloc["count"][jjbankloc['locations'].str.contains('gurgaon|gurugram|mumbai', regex=True)].sum()
    banklocations["mumbai"]=jjbankloc["count"][jjbankloc['locations'].str.contains('mumbai', regex=True)].sum()
    from operator import itemgetter
    banklocations=dict(sorted(banklocations.items(), key=itemgetter(1),reverse=True))

    random_x=list(banklocations.keys())
    random_y=list(banklocations.values())
    plot = px.Figure(data=[px.Bar( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Banking Locations"
                        ,x=0.5),xaxis_title="Banking Locations",yaxis_title="Jobs"))
    plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ), 
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    )
                ]), 
                direction="down", 
            ), 
        ] 
    )
    #plot.show()
    plot.write_html(r"templates\charts\banking_c3.html",full_html=False,include_plotlyjs='cdn')


    # SALES ********************************************************************************************************************

    salesdf=df.loc[(df['Role_Category']=='enterprise & b2b sales')|(df['Role_Category']=='retail & b2c sales')|(df['Role_Category']=='bd / pre sales')]

    salesdf["Min_Exp"].value_counts()[:10].plot.barh(figsize=(8,5),fontsize=13,color="b")
    df2=pd.DataFrame(salesdf.Min_Exp.apply(pd.Series).stack().value_counts()[:10]).reset_index()
    df2.columns=["Min_Exp","count"]
    random_x=list(df2["Min_Exp"])
    random_y=list(df2["count"])
    plot = px.Figure(data=[px.Line( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Min Experience for Sales"
                        ,x=0.5),xaxis_title="Min_Exp",yaxis_title="Jobs"))
    plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    ),
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ),
                ]), 
                direction="down", 
            ), 
        ] 
    ) 
    #plot.show()
    plot.write_html(r"templates\charts\sales_c1.html",full_html=False,include_plotlyjs='cdn')


    jjsales=pd.DataFrame(salesdf.Skills.apply(pd.Series).stack().value_counts()).reset_index()
    jjsales.columns=["skills","count"]

    sales={}
    #maintainance troubleshooting communication-skills supervise management operations
    sales['b2b sales']=jjsales["count"][jjsales['skills'].str.contains('sales|b2b sales|corporate sales|direct sales|international sales', regex=True)].sum()
    sales['b2c sales']=jjsales["count"][jjsales['skills'].str.contains('sales|b2c sales|field sales|direct sales|communication skills|sales and marketing|inside sales', regex=True)].sum()
    sales['management']=jjsales["count"][jjsales['skills'].str.contains('business management|sales management|communication skills|team management|sales strategy|operations', regex=True)].sum()
    sales['team management']=jjsales["count"][jjsales['skills'].str.contains('marketing|sales and marketing|lead generation|business development management|key account management|revenue generation', regex=True)].sum()
    sales['client management']=jjsales["count"][jjsales['skills'].str.contains('client relationship|customer service|customer relationship|relationship|financial services|client meeting|client management', regex=True)].sum()

    from operator import itemgetter
    sales=dict(sorted(sales.items(), key=itemgetter(1),reverse=True))
    random_x=list(sales.keys())
    random_y=list(sales.values())
    plot = px.Figure(data=[px.Pie(labels=random_x,values=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Sales Must Have Skills"
                        ,x=0.5),xaxis_title="Sales Skills",yaxis_title="Jobs"))
    #plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ), 
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    )
                ]), 
                direction="down", 
            ), 
        ] 
    )
    #plot.show()
    plot.write_html(r"templates\charts\sales_c2.html",full_html=False,include_plotlyjs='cdn')


    jjsalesloc=pd.DataFrame(salesdf.Location.apply(pd.Series).stack().value_counts()).reset_index()
    jjsalesloc.columns=["locations","count"]
    saleslocations={}
    saleslocations["noida"]=jjsalesloc["count"][jjsalesloc['locations'].str.contains('Noida|noida', regex=True)].sum()
    saleslocations["bangalore"]=jjsalesloc["count"][jjsalesloc['locations'].str.contains('Bangalore|Bengaluru|bangalore|bengaluru', regex=True)].sum()
    saleslocations["chennai"]=jjsalesloc["count"][jjsalesloc['locations'].str.contains('Chennai|chennai', regex=True)].sum()
    saleslocations["cochin"]=jjsalesloc["count"][jjsalesloc['locations'].str.contains('cochin|kochi', regex=True)].sum()
    saleslocations["gurugram"]=jjsalesloc["count"][jjsalesloc['locations'].str.contains('Gurgoan|Gurugram|gurgoan|gurugram|faridabad', regex=True)].sum()
    saleslocations["mumbai"]=jjsalesloc["count"][jjsalesloc['locations'].str.contains('Mumbai|mumbai', regex=True)].sum()
    saleslocations["pune"]=jjsalesloc["count"][jjsalesloc['locations'].str.contains('Pune|pune', regex=True)].sum()
    saleslocations["hyderabad"]=jjsalesloc["count"][jjsalesloc['locations'].str.contains('Hyderabad|hyderabad', regex=True)].sum()
    saleslocations["delhi"]=jjsalesloc["count"][jjsalesloc['locations'].str.contains('New Delhi|delhi|ncr', regex=True)].sum()
    saleslocations["kolkata"]=jjsalesloc["count"][jjsalesloc['locations'].str.contains('Kolkata|kolkata', regex=True)].sum()
    saleslocations["chandigarh"]=jjsalesloc["count"][jjsalesloc['locations'].str.contains('Chandigarh|chandigarh', regex=True)].sum()
    from operator import itemgetter
    saleslocations=dict(sorted(saleslocations.items(), key=itemgetter(1),reverse=True))
    random_x=list(saleslocations.keys())
    random_y=list(saleslocations.values())
    plot = px.Figure(data=[px.Bar( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Sales Location"
                        ,x=0.5),xaxis_title="Sales Location",yaxis_title="Jobs"))
    plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ), 
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    )
                ]), 
                direction="down", 
            ), 
        ] 
    )  
    #plot.show()
    plot.write_html(r"templates\charts\sales_c3.html",full_html=False,include_plotlyjs='cdn')

    df2=pd.DataFrame(salesdf.Role.apply(pd.Series).stack().value_counts()[:10]).reset_index()
    df2.columns=["Role","count"]
    random_x=list(df2["Role"])
    random_y=list(df2["count"])
    plot = px.Figure(data=[px.Bar( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Types of Sales Roles"
                        ,x=0.5),xaxis_title="Roles",yaxis_title="Jobs"))
    #Add dropdown 
    plot.update_traces(marker_color=sample_colors)
    plot.update_layout( 
        updatemenus=[ 
            dict( 
                buttons=list([ 
                    dict( 
                        args=["type", "bar"], 
                        label="Bar Chart", 
                        method="restyle",
                    ) ,  
                    dict( 
                        args=["type", "pie"], 
                        label="Pie Chart", 
                        method="restyle"
                    ), 
                    dict( 
                        args=["type", "line"], 
                        label="Line Plot", 
                        method="restyle"
                    )
                ]), 
                direction="down", 
            ), 
        ] 
    ) 
    #plot.show()
    plot.write_html(r"templates\charts\sales_c4.html",full_html=False,include_plotlyjs='cdn')

def operate_the_functions():
    d0=[]
    d1=[]
    d2=[]
    d3=[]
    d4=[]
    d5=[]
    d6=[]
    d7=[]
    d8=[]
    d9=[]
    d10=[]
    d11=[]
    valueList=[d0,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11]
    columnList=['Title','Company','Role','Industry_Type','Department','Role_Category','Experience','Benefits','Location','Skills','URL','Job_Description']
    sample_colors=["#FE6363","#66FA72","#6B89F9","orchid","yellow","pink","slategrey","burlywood","firebrick","indigo","khaki"]
    
    conn = sqlite.connect(r'data\example.db')
    with conn:
        conn.row_factory = sqlite.Row
        curs = conn.cursor()
        curs.execute("SELECT * FROM sample")
        rows = curs.fetchall()
        for row in rows:
            for i in range(0,12):
                valueList[i].append(row[columnList[i]])
    diction={}
    for i in range(0,12):
        diction[columnList[i]]=valueList[i]
    df=pd.DataFrame(diction)
    
    df=clean_dataset(df)
    analyse_and_visualize(df,sample_colors)


#Executing
#operate_the_functions()