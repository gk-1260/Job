import sqlite3 as sqlite
import pandas as pd
import plotly.graph_objects as px 


def clean_dataset_location(df:pd.DataFrame):
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

def analyse_and_visualize_location(df:pd.DataFrame,sample_colors:list):

    # NOIDA ********************************************************************************************************************
    noidadf = df[df['Location'].str.contains('noida')]

    noidadf["Min_Exp"].value_counts()[:10].plot.barh(figsize=(8,5),fontsize=13,color="b")
    df2=pd.DataFrame(noidadf.Min_Exp.apply(pd.Series).stack().value_counts()[:10]).reset_index()
    df2.columns=["Min_Exp","count"]
    random_x=list(df2["Min_Exp"])
    random_y=list(df2["count"])
    plot = px.Figure(data=[px.Line( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Min Experience in Noida"
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
    plot.write_html(r"templates\charts\noida_c1.html",full_html=False,include_plotlyjs='cdn')


    jjnoidafield=pd.DataFrame(noidadf.Role_Category.apply(pd.Series).stack().value_counts()).reset_index()
    jjnoidafield.columns=["fields","count"]
    noidafield={}
    noidafield["data science & machine learning"]=jjnoidafield["count"][jjnoidafield['fields'].str.contains('data science & machine learning', regex=True)].sum()
    noidafield["engineering"]=jjnoidafield["count"][jjnoidafield['fields'].str.contains('engineering', regex=True)].sum()
    noidafield["hr"]=jjnoidafield["count"][jjnoidafield['fields'].str.contains('hr operations', regex=True)].sum()
    noidafield["support"]=jjnoidafield["count"][jjnoidafield['fields'].str.contains('operations, maintenance & support|sales support & operations|surveying', regex=True)].sum()
    noidafield["finance"]=jjnoidafield["count"][jjnoidafield['fields'].str.contains('finance|finance & accounting - other|accounting & taxation|treasury', regex=True)].sum()
    noidafield["business intelligence & analytics"]=jjnoidafield["count"][jjnoidafield['fields'].str.contains('business intelligence & analytics', regex=True)].sum()
    noidafield["management"]=jjnoidafield["count"][jjnoidafield['fields'].str.contains('management', regex=True)].sum()
    noidafield["banking"]=jjnoidafield["count"][jjnoidafield['fields'].str.contains('investment banking, private equity & vc|trading, asset & wealth management|banking operation|bfsi, investments & trading', regex=True)].sum()
    noidafield["sales"]=jjnoidafield["count"][jjnoidafield['fields'].str.contains('enterprise & b2b sales|retail & b2c sales|bd / pre sales', regex=True)].sum()
    from operator import itemgetter
    noidafield=dict(sorted(noidafield.items(), key=itemgetter(1),reverse=True))

    random_x=list(noidafield.keys())
    random_y=list(noidafield.values())
    plot = px.Figure(data=[px.Bar( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Noida Fields"
                        ,x=0.5),xaxis_title="Fields",yaxis_title="Jobs"))
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
    plot.write_html(r"templates\charts\noida_c2.html",full_html=False,include_plotlyjs='cdn')
    
    # Bangalore ********************************************************************************************************************
    bangaloredf = df[df['Location'].str.contains('bangalore')]

    bangaloredf["Min_Exp"].value_counts()[:10].plot.barh(figsize=(8,5),fontsize=13,color="b")
    df2=pd.DataFrame(bangaloredf.Min_Exp.apply(pd.Series).stack().value_counts()[:10]).reset_index()
    df2.columns=["Min_Exp","count"]
    random_x=list(df2["Min_Exp"])
    random_y=list(df2["count"])
    plot = px.Figure(data=[px.Line( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Min Experience in Bangalore"
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
    plot.write_html(r"templates\charts\bangalore_c1.html",full_html=False,include_plotlyjs='cdn')


    jjbangalorefield=pd.DataFrame(bangaloredf.Role_Category.apply(pd.Series).stack().value_counts()).reset_index()
    jjbangalorefield.columns=["fields","count"]
    bangalorefield={}
    bangalorefield["data science & machine learning"]=jjbangalorefield["count"][jjbangalorefield['fields'].str.contains('data science & machine learning', regex=True)].sum()
    bangalorefield["engineering"]=jjbangalorefield["count"][jjbangalorefield['fields'].str.contains('engineering', regex=True)].sum()
    bangalorefield["hr"]=jjbangalorefield["count"][jjbangalorefield['fields'].str.contains('hr operations', regex=True)].sum()
    bangalorefield["support"]=jjbangalorefield["count"][jjbangalorefield['fields'].str.contains('operations, maintenance & support|sales support & operations|surveying', regex=True)].sum()
    bangalorefield["finance"]=jjbangalorefield["count"][jjbangalorefield['fields'].str.contains('finance|finance & accounting - other|accounting & taxation|treasury', regex=True)].sum()
    bangalorefield["business intelligence & analytics"]=jjbangalorefield["count"][jjbangalorefield['fields'].str.contains('business intelligence & analytics', regex=True)].sum()
    bangalorefield["management"]=jjbangalorefield["count"][jjbangalorefield['fields'].str.contains('management', regex=True)].sum()
    bangalorefield["banking"]=jjbangalorefield["count"][jjbangalorefield['fields'].str.contains('investment banking, private equity & vc|trading, asset & wealth management|banking operation|bfsi, investments & trading', regex=True)].sum()
    bangalorefield["sales"]=jjbangalorefield["count"][jjbangalorefield['fields'].str.contains('enterprise & b2b sales|retail & b2c sales|bd / pre sales', regex=True)].sum()
    from operator import itemgetter
    bangalorefield=dict(sorted(bangalorefield.items(), key=itemgetter(1),reverse=True))

    random_x=list(bangalorefield.keys())
    random_y=list(bangalorefield.values())
    plot = px.Figure(data=[px.Bar( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Bangalore Fields"
                        ,x=0.5),xaxis_title="Fields",yaxis_title="Jobs"))
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
    plot.write_html(r"templates\charts\bangalore_c2.html",full_html=False,include_plotlyjs='cdn')
    
    # Chennai ********************************************************************************************************************
    chennaidf = df[df['Location'].str.contains('chennai')]

    chennaidf["Min_Exp"].value_counts()[:10].plot.barh(figsize=(8,5),fontsize=13,color="b")
    df2=pd.DataFrame(chennaidf.Min_Exp.apply(pd.Series).stack().value_counts()[:10]).reset_index()
    df2.columns=["Min_Exp","count"]
    random_x=list(df2["Min_Exp"])
    random_y=list(df2["count"])
    plot = px.Figure(data=[px.Line( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Min Experience in Chennai"
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
    plot.write_html(r"templates\charts\chennai_c1.html",full_html=False,include_plotlyjs='cdn')


    jjchennaifield=pd.DataFrame(chennaidf.Role_Category.apply(pd.Series).stack().value_counts()).reset_index()
    jjchennaifield.columns=["fields","count"]
    chennaifield={}
    chennaifield["data science & machine learning"]=jjchennaifield["count"][jjchennaifield['fields'].str.contains('data science & machine learning', regex=True)].sum()
    chennaifield["engineering"]=jjchennaifield["count"][jjchennaifield['fields'].str.contains('engineering', regex=True)].sum()
    chennaifield["hr"]=jjchennaifield["count"][jjchennaifield['fields'].str.contains('hr operations', regex=True)].sum()
    chennaifield["support"]=jjchennaifield["count"][jjchennaifield['fields'].str.contains('operations, maintenance & support|sales support & operations|surveying', regex=True)].sum()
    chennaifield["finance"]=jjchennaifield["count"][jjchennaifield['fields'].str.contains('finance|finance & accounting - other|accounting & taxation|treasury', regex=True)].sum()
    chennaifield["business intelligence & analytics"]=jjchennaifield["count"][jjchennaifield['fields'].str.contains('business intelligence & analytics', regex=True)].sum()
    chennaifield["management"]=jjchennaifield["count"][jjchennaifield['fields'].str.contains('management', regex=True)].sum()
    chennaifield["banking"]=jjchennaifield["count"][jjchennaifield['fields'].str.contains('investment banking, private equity & vc|trading, asset & wealth management|banking operation|bfsi, investments & trading', regex=True)].sum()
    chennaifield["sales"]=jjchennaifield["count"][jjchennaifield['fields'].str.contains('enterprise & b2b sales|retail & b2c sales|bd / pre sales', regex=True)].sum()
    from operator import itemgetter
    chennaifield=dict(sorted(chennaifield.items(), key=itemgetter(1),reverse=True))

    random_x=list(chennaifield.keys())
    random_y=list(chennaifield.values())
    plot = px.Figure(data=[px.Bar( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Chennai Fields"
                        ,x=0.5),xaxis_title="Fields",yaxis_title="Jobs"))
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
    plot.write_html(r"templates\charts\chennai_c2.html",full_html=False,include_plotlyjs='cdn')

    
    # Remote ********************************************************************************************************************
    remotedf = df[df['Location'].str.contains('remote')]

    remotedf["Min_Exp"].value_counts()[:10].plot.barh(figsize=(8,5),fontsize=13,color="b")
    df2=pd.DataFrame(remotedf.Min_Exp.apply(pd.Series).stack().value_counts()[:10]).reset_index()
    df2.columns=["Min_Exp","count"]
    random_x=list(df2["Min_Exp"])
    random_y=list(df2["count"])
    plot = px.Figure(data=[px.Line( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Min Experience in Remote Work"
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
    plot.write_html(r"templates\charts\remote_c1.html",full_html=False,include_plotlyjs='cdn')


    jjremotefield=pd.DataFrame(remotedf.Role_Category.apply(pd.Series).stack().value_counts()).reset_index()
    jjremotefield.columns=["fields","count"]
    remotefield={}
    remotefield["data science & machine learning"]=jjremotefield["count"][jjremotefield['fields'].str.contains('data science & machine learning', regex=True)].sum()
    remotefield["engineering"]=jjremotefield["count"][jjremotefield['fields'].str.contains('engineering', regex=True)].sum()
    remotefield["hr"]=jjremotefield["count"][jjremotefield['fields'].str.contains('hr operations', regex=True)].sum()
    remotefield["support"]=jjremotefield["count"][jjremotefield['fields'].str.contains('operations, maintenance & support|sales support & operations|surveying', regex=True)].sum()
    remotefield["finance"]=jjremotefield["count"][jjremotefield['fields'].str.contains('finance|finance & accounting - other|accounting & taxation|treasury', regex=True)].sum()
    remotefield["business intelligence & analytics"]=jjremotefield["count"][jjremotefield['fields'].str.contains('business intelligence & analytics', regex=True)].sum()
    remotefield["management"]=jjremotefield["count"][jjremotefield['fields'].str.contains('management', regex=True)].sum()
    remotefield["banking"]=jjremotefield["count"][jjremotefield['fields'].str.contains('investment banking, private equity & vc|trading, asset & wealth management|banking operation|bfsi, investments & trading', regex=True)].sum()
    remotefield["sales"]=jjremotefield["count"][jjremotefield['fields'].str.contains('enterprise & b2b sales|retail & b2c sales|bd / pre sales', regex=True)].sum()
    from operator import itemgetter
    remotefield=dict(sorted(remotefield.items(), key=itemgetter(1),reverse=True))

    random_x=list(remotefield.keys())
    random_y=list(remotefield.values())
    plot = px.Figure(data=[px.Bar( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Remote Fields"
                        ,x=0.5),xaxis_title="Fields",yaxis_title="Jobs"))
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
    plot.write_html(r"templates\charts\remote_c2.html",full_html=False,include_plotlyjs='cdn')
    
    # Gurugram ********************************************************************************************************************
    gurugramdf = df[df['Location'].str.contains('gurgaon|gurugram')]

    gurugramdf["Min_Exp"].value_counts()[:10].plot.barh(figsize=(8,5),fontsize=13,color="b")
    df2=pd.DataFrame(gurugramdf.Min_Exp.apply(pd.Series).stack().value_counts()[:10]).reset_index()
    df2.columns=["Min_Exp","count"]
    random_x=list(df2["Min_Exp"])
    random_y=list(df2["count"])
    plot = px.Figure(data=[px.Line( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Min Experience in Gurugram"
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
    plot.write_html(r"templates\charts\gurugram_c1.html",full_html=False,include_plotlyjs='cdn')


    jjgurugramfield=pd.DataFrame(gurugramdf.Role_Category.apply(pd.Series).stack().value_counts()).reset_index()
    jjgurugramfield.columns=["fields","count"]
    gurugramfield={}
    gurugramfield["data science & machine learning"]=jjgurugramfield["count"][jjgurugramfield['fields'].str.contains('data science & machine learning', regex=True)].sum()
    gurugramfield["engineering"]=jjgurugramfield["count"][jjgurugramfield['fields'].str.contains('engineering', regex=True)].sum()
    gurugramfield["hr"]=jjgurugramfield["count"][jjgurugramfield['fields'].str.contains('hr operations', regex=True)].sum()
    gurugramfield["support"]=jjgurugramfield["count"][jjgurugramfield['fields'].str.contains('operations, maintenance & support|sales support & operations|surveying', regex=True)].sum()
    gurugramfield["finance"]=jjgurugramfield["count"][jjgurugramfield['fields'].str.contains('finance|finance & accounting - other|accounting & taxation|treasury', regex=True)].sum()
    gurugramfield["business intelligence & analytics"]=jjgurugramfield["count"][jjgurugramfield['fields'].str.contains('business intelligence & analytics', regex=True)].sum()
    gurugramfield["management"]=jjgurugramfield["count"][jjgurugramfield['fields'].str.contains('management', regex=True)].sum()
    gurugramfield["banking"]=jjgurugramfield["count"][jjgurugramfield['fields'].str.contains('investment banking, private equity & vc|trading, asset & wealth management|banking operation|bfsi, investments & trading', regex=True)].sum()
    gurugramfield["sales"]=jjgurugramfield["count"][jjgurugramfield['fields'].str.contains('enterprise & b2b sales|retail & b2c sales|bd / pre sales', regex=True)].sum()
    from operator import itemgetter
    gurugramfield=dict(sorted(gurugramfield.items(), key=itemgetter(1),reverse=True))

    random_x=list(gurugramfield.keys())
    random_y=list(gurugramfield.values())
    plot = px.Figure(data=[px.Bar( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Gurugram Fields"
                        ,x=0.5),xaxis_title="Fields",yaxis_title="Jobs"))
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
    plot.write_html(r"templates\charts\gurugram_c2.html",full_html=False,include_plotlyjs='cdn')

    # Mumbai ********************************************************************************************************************
    mumbaidf = df[df['Location'].str.contains('mumbai')]

    mumbaidf["Min_Exp"].value_counts()[:10].plot.barh(figsize=(8,5),fontsize=13,color="b")
    df2=pd.DataFrame(mumbaidf.Min_Exp.apply(pd.Series).stack().value_counts()[:10]).reset_index()
    df2.columns=["Min_Exp","count"]
    random_x=list(df2["Min_Exp"])
    random_y=list(df2["count"])
    plot = px.Figure(data=[px.Line( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Min Experience in Mumbai"
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
    plot.write_html(r"templates\charts\mumbai_c1.html",full_html=False,include_plotlyjs='cdn')


    jjmumbaifield=pd.DataFrame(mumbaidf.Role_Category.apply(pd.Series).stack().value_counts()).reset_index()
    jjmumbaifield.columns=["fields","count"]
    mumbaifield={}
    mumbaifield["data science & machine learning"]=jjmumbaifield["count"][jjmumbaifield['fields'].str.contains('data science & machine learning', regex=True)].sum()
    mumbaifield["engineering"]=jjmumbaifield["count"][jjmumbaifield['fields'].str.contains('engineering', regex=True)].sum()
    mumbaifield["hr"]=jjmumbaifield["count"][jjmumbaifield['fields'].str.contains('hr operations', regex=True)].sum()
    mumbaifield["support"]=jjmumbaifield["count"][jjmumbaifield['fields'].str.contains('operations, maintenance & support|sales support & operations|surveying', regex=True)].sum()
    mumbaifield["finance"]=jjmumbaifield["count"][jjmumbaifield['fields'].str.contains('finance|finance & accounting - other|accounting & taxation|treasury', regex=True)].sum()
    mumbaifield["business intelligence & analytics"]=jjmumbaifield["count"][jjmumbaifield['fields'].str.contains('business intelligence & analytics', regex=True)].sum()
    mumbaifield["management"]=jjmumbaifield["count"][jjmumbaifield['fields'].str.contains('management', regex=True)].sum()
    mumbaifield["banking"]=jjmumbaifield["count"][jjmumbaifield['fields'].str.contains('investment banking, private equity & vc|trading, asset & wealth management|banking operation|bfsi, investments & trading', regex=True)].sum()
    mumbaifield["sales"]=jjmumbaifield["count"][jjmumbaifield['fields'].str.contains('enterprise & b2b sales|retail & b2c sales|bd / pre sales', regex=True)].sum()
    from operator import itemgetter
    mumbaifield=dict(sorted(mumbaifield.items(), key=itemgetter(1),reverse=True))

    random_x=list(mumbaifield.keys())
    random_y=list(mumbaifield.values())
    plot = px.Figure(data=[px.Bar( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Mumbai Fields"
                        ,x=0.5),xaxis_title="Fields",yaxis_title="Jobs"))
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
    plot.write_html(r"templates\charts\mumbai_c2.html",full_html=False,include_plotlyjs='cdn')

    # PUNE ********************************************************************************************************************
    punedf = df[df['Location'].str.contains('pune')]

    punedf["Min_Exp"].value_counts()[:10].plot.barh(figsize=(8,5),fontsize=13,color="b")
    df2=pd.DataFrame(punedf.Min_Exp.apply(pd.Series).stack().value_counts()[:10]).reset_index()
    df2.columns=["Min_Exp","count"]
    random_x=list(df2["Min_Exp"])
    random_y=list(df2["count"])
    plot = px.Figure(data=[px.Line( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Min Experience in Pune"
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
    plot.write_html(r"templates\charts\pune_c1.html",full_html=False,include_plotlyjs='cdn')


    jjpunefield=pd.DataFrame(punedf.Role_Category.apply(pd.Series).stack().value_counts()).reset_index()
    jjpunefield.columns=["fields","count"]
    punefield={}
    punefield["data science & machine learning"]=jjpunefield["count"][jjpunefield['fields'].str.contains('data science & machine learning', regex=True)].sum()
    punefield["engineering"]=jjpunefield["count"][jjpunefield['fields'].str.contains('engineering', regex=True)].sum()
    punefield["hr"]=jjpunefield["count"][jjpunefield['fields'].str.contains('hr operations', regex=True)].sum()
    punefield["support"]=jjpunefield["count"][jjpunefield['fields'].str.contains('operations, maintenance & support|sales support & operations|surveying', regex=True)].sum()
    punefield["finance"]=jjpunefield["count"][jjpunefield['fields'].str.contains('finance|finance & accounting - other|accounting & taxation|treasury', regex=True)].sum()
    punefield["business intelligence & analytics"]=jjpunefield["count"][jjpunefield['fields'].str.contains('business intelligence & analytics', regex=True)].sum()
    punefield["management"]=jjpunefield["count"][jjpunefield['fields'].str.contains('management', regex=True)].sum()
    punefield["banking"]=jjpunefield["count"][jjpunefield['fields'].str.contains('investment banking, private equity & vc|trading, asset & wealth management|banking operation|bfsi, investments & trading', regex=True)].sum()
    punefield["sales"]=jjpunefield["count"][jjpunefield['fields'].str.contains('enterprise & b2b sales|retail & b2c sales|bd / pre sales', regex=True)].sum()
    from operator import itemgetter
    punefield=dict(sorted(punefield.items(), key=itemgetter(1),reverse=True))

    random_x=list(punefield.keys())
    random_y=list(punefield.values())
    plot = px.Figure(data=[px.Bar( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Pune Fields"
                        ,x=0.5),xaxis_title="Fields",yaxis_title="Jobs"))
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
    plot.write_html(r"templates\charts\pune_c2.html",full_html=False,include_plotlyjs='cdn')

    # HYDERABAD ********************************************************************************************************************
    hyddf = df[df['Location'].str.contains('hyderabad')]

    hyddf["Min_Exp"].value_counts()[:10].plot.barh(figsize=(8,5),fontsize=13,color="b")
    df2=pd.DataFrame(hyddf.Min_Exp.apply(pd.Series).stack().value_counts()[:10]).reset_index()
    df2.columns=["Min_Exp","count"]
    random_x=list(df2["Min_Exp"])
    random_y=list(df2["count"])
    plot = px.Figure(data=[px.Line( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Min Experience in Hyderabad"
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
    plot.write_html(r"templates\charts\hyderabad_c1.html",full_html=False,include_plotlyjs='cdn')


    jjhydfield=pd.DataFrame(hyddf.Role_Category.apply(pd.Series).stack().value_counts()).reset_index()
    jjhydfield.columns=["fields","count"]
    hydfield={}
    hydfield["data science & machine learning"]=jjhydfield["count"][jjhydfield['fields'].str.contains('data science & machine learning', regex=True)].sum()
    hydfield["engineering"]=jjhydfield["count"][jjhydfield['fields'].str.contains('engineering', regex=True)].sum()
    hydfield["hr"]=jjhydfield["count"][jjhydfield['fields'].str.contains('hr operations', regex=True)].sum()
    hydfield["support"]=jjhydfield["count"][jjhydfield['fields'].str.contains('operations, maintenance & support|sales support & operations|surveying', regex=True)].sum()
    hydfield["finance"]=jjhydfield["count"][jjhydfield['fields'].str.contains('finance|finance & accounting - other|accounting & taxation|treasury', regex=True)].sum()
    hydfield["business intelligence & analytics"]=jjhydfield["count"][jjhydfield['fields'].str.contains('business intelligence & analytics', regex=True)].sum()
    hydfield["management"]=jjhydfield["count"][jjhydfield['fields'].str.contains('management', regex=True)].sum()
    hydfield["banking"]=jjhydfield["count"][jjhydfield['fields'].str.contains('investment banking, private equity & vc|trading, asset & wealth management|banking operation|bfsi, investments & trading', regex=True)].sum()
    hydfield["sales"]=jjhydfield["count"][jjhydfield['fields'].str.contains('enterprise & b2b sales|retail & b2c sales|bd / pre sales', regex=True)].sum()
    from operator import itemgetter
    hydfield=dict(sorted(hydfield.items(), key=itemgetter(1),reverse=True))

    random_x=list(hydfield.keys())
    random_y=list(hydfield.values())
    plot = px.Figure(data=[px.Bar( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Hyderabad Fields"
                        ,x=0.5),xaxis_title="Fields",yaxis_title="Jobs"))
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
    plot.write_html(r"templates\charts\hyderabad_c2.html",full_html=False,include_plotlyjs='cdn')

    # DELHI ********************************************************************************************************************
    deldf = df[df['Location'].str.contains('new delhi|delhi')]

    deldf["Min_Exp"].value_counts()[:10].plot.barh(figsize=(8,5),fontsize=13,color="b")
    df2=pd.DataFrame(deldf.Min_Exp.apply(pd.Series).stack().value_counts()[:10]).reset_index()
    df2.columns=["Min_Exp","count"]
    random_x=list(df2["Min_Exp"])
    random_y=list(df2["count"])
    plot = px.Figure(data=[px.Line( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Min Experience in Delhi"
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
    plot.write_html(r"templates\charts\delhi_c1.html",full_html=False,include_plotlyjs='cdn')


    jjdelfield=pd.DataFrame(deldf.Role_Category.apply(pd.Series).stack().value_counts()).reset_index()
    jjdelfield.columns=["fields","count"]
    delfield={}
    delfield["data science & machine learning"]=jjdelfield["count"][jjdelfield['fields'].str.contains('data science & machine learning', regex=True)].sum()
    delfield["engineering"]=jjdelfield["count"][jjdelfield['fields'].str.contains('engineering', regex=True)].sum()
    delfield["hr"]=jjdelfield["count"][jjdelfield['fields'].str.contains('hr operations', regex=True)].sum()
    delfield["support"]=jjdelfield["count"][jjdelfield['fields'].str.contains('operations, maintenance & support|sales support & operations|surveying', regex=True)].sum()
    delfield["finance"]=jjdelfield["count"][jjdelfield['fields'].str.contains('finance|finance & accounting - other|accounting & taxation|treasury', regex=True)].sum()
    hydfield["business intelligence & analytics"]=jjdelfield["count"][jjdelfield['fields'].str.contains('business intelligence & analytics', regex=True)].sum()
    delfield["management"]=jjdelfield["count"][jjdelfield['fields'].str.contains('management', regex=True)].sum()
    delfield["banking"]=jjdelfield["count"][jjdelfield['fields'].str.contains('investment banking, private equity & vc|trading, asset & wealth management|banking operation|bfsi, investments & trading', regex=True)].sum()
    delfield["sales"]=jjdelfield["count"][jjdelfield['fields'].str.contains('enterprise & b2b sales|retail & b2c sales|bd / pre sales', regex=True)].sum()
    from operator import itemgetter
    delfield=dict(sorted(delfield.items(), key=itemgetter(1),reverse=True))

    random_x=list(delfield.keys())
    random_y=list(delfield.values())
    plot = px.Figure(data=[px.Bar( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Delhi Fields"
                        ,x=0.5),xaxis_title="Fields",yaxis_title="Jobs"))
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
    plot.write_html(r"templates\charts\delhi_c2.html",full_html=False,include_plotlyjs='cdn')

    # KOLKATA ********************************************************************************************************************
    koldf = df[df['Location'].str.contains('kolkata|calcutta')]

    koldf["Min_Exp"].value_counts()[:10].plot.barh(figsize=(8,5),fontsize=13,color="b")
    df2=pd.DataFrame(koldf.Min_Exp.apply(pd.Series).stack().value_counts()[:10]).reset_index()
    df2.columns=["Min_Exp","count"]
    random_x=list(df2["Min_Exp"])
    random_y=list(df2["count"])
    plot = px.Figure(data=[px.Line( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Min Experience in Kolkata"
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
    plot.write_html(r"templates\charts\kolkata_c1.html",full_html=False,include_plotlyjs='cdn')


    jjkolfield=pd.DataFrame(koldf.Role_Category.apply(pd.Series).stack().value_counts()).reset_index()
    jjkolfield.columns=["fields","count"]
    kolfield={}
    kolfield["data science & machine learning"]=jjkolfield["count"][jjkolfield['fields'].str.contains('data science & machine learning', regex=True)].sum()
    kolfield["engineering"]=jjkolfield["count"][jjkolfield['fields'].str.contains('engineering', regex=True)].sum()
    kolfield["hr"]=jjkolfield["count"][jjkolfield['fields'].str.contains('hr operations', regex=True)].sum()
    kolfield["support"]=jjkolfield["count"][jjkolfield['fields'].str.contains('operations, maintenance & support|sales support & operations|surveying', regex=True)].sum()
    kolfield["finance"]=jjkolfield["count"][jjkolfield['fields'].str.contains('finance|finance & accounting - other|accounting & taxation|treasury', regex=True)].sum()
    kolfield["business intelligence & analytics"]=jjkolfield["count"][jjkolfield['fields'].str.contains('business intelligence & analytics', regex=True)].sum()
    kolfield["management"]=jjkolfield["count"][jjkolfield['fields'].str.contains('management', regex=True)].sum()
    kolfield["banking"]=jjkolfield["count"][jjkolfield['fields'].str.contains('investment banking, private equity & vc|trading, asset & wealth management|banking operation|bfsi, investments & trading', regex=True)].sum()
    kolfield["sales"]=jjkolfield["count"][jjkolfield['fields'].str.contains('enterprise & b2b sales|retail & b2c sales|bd / pre sales', regex=True)].sum()
    from operator import itemgetter
    kolfield=dict(sorted(kolfield.items(), key=itemgetter(1),reverse=True))

    random_x=list(kolfield.keys())
    random_y=list(kolfield.values())
    plot = px.Figure(data=[px.Bar( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Kolkata Fields"
                        ,x=0.5),xaxis_title="Fields",yaxis_title="Jobs"))
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
    plot.write_html(r"templates\charts\kolkata_c2.html",full_html=False,include_plotlyjs='cdn')
    
    # CHANDIGARH ********************************************************************************************************************
    chdf = df[df['Location'].str.contains('chandigarh')]

    chdf["Min_Exp"].value_counts()[:10].plot.barh(figsize=(8,5),fontsize=13,color="b")
    df2=pd.DataFrame(chdf.Min_Exp.apply(pd.Series).stack().value_counts()[:10]).reset_index()
    df2.columns=["Min_Exp","count"]
    random_x=list(df2["Min_Exp"])
    random_y=list(df2["count"])
    plot = px.Figure(data=[px.Line( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Min Experience in Chandigarh"
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
    plot.write_html(r"templates\charts\chandigarh_c1.html",full_html=False,include_plotlyjs='cdn')


    jjchfield=pd.DataFrame(chdf.Role_Category.apply(pd.Series).stack().value_counts()).reset_index()
    jjchfield.columns=["fields","count"]
    chfield={}
    chfield["data science & machine learning"]=jjchfield["count"][jjchfield['fields'].str.contains('data science & machine learning', regex=True)].sum()
    chfield["engineering"]=jjchfield["count"][jjchfield['fields'].str.contains('engineering', regex=True)].sum()
    chfield["hr"]=jjchfield["count"][jjchfield['fields'].str.contains('hr operations', regex=True)].sum()
    chfield["support"]=jjchfield["count"][jjchfield['fields'].str.contains('operations, maintenance & support|sales support & operations|surveying', regex=True)].sum()
    chfield["finance"]=jjchfield["count"][jjchfield['fields'].str.contains('finance|finance & accounting - other|accounting & taxation|treasury', regex=True)].sum()
    chfield["business intelligence & analytics"]=jjchfield["count"][jjchfield['fields'].str.contains('business intelligence & analytics', regex=True)].sum()
    chfield["management"]=jjchfield["count"][jjchfield['fields'].str.contains('management', regex=True)].sum()
    chfield["banking"]=jjchfield["count"][jjchfield['fields'].str.contains('investment banking, private equity & vc|trading, asset & wealth management|banking operation|bfsi, investments & trading', regex=True)].sum()
    chfield["sales"]=jjchfield["count"][jjchfield['fields'].str.contains('enterprise & b2b sales|retail & b2c sales|bd / pre sales', regex=True)].sum()
    from operator import itemgetter
    chfield=dict(sorted(chfield.items(), key=itemgetter(1),reverse=True))

    random_x=list(chfield.keys())
    random_y=list(chfield.values())
    plot = px.Figure(data=[px.Bar( x=random_x, y=random_y)],
                    layout=px.Layout(title=px.layout.Title(
                        text="Chandigarh Fields"
                        ,x=0.5),xaxis_title="Fields",yaxis_title="Jobs"))
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
    plot.write_html(r"templates\charts\chandigarh_c2.html",full_html=False,include_plotlyjs='cdn')


def operate_the_functions_location():
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
    
    df=clean_dataset_location(df)
    analyse_and_visualize_location(df,sample_colors)


#Executing
#operate_the_functions_location()