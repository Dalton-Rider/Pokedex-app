import streamlit as st
import info2
import pandas as pd
import matplotlib.pyplot as plt


def main_section():
    st.header("🔎Find Your Pokemon!")
    st.image(info2.main_image, width=200)
    st.write(info2.about_app)
    st.write("---")
main_section()

newlist = []
newlist2 = []
newlist3 = []

def type_section():
    #new
    option = st.selectbox(
        'What type do you want?🔥💧🌿',
        ('fire','grass','water','flying','normal','poison','dragon','ice','electric','ground','fighting','psychic','bug','ghost','rock'))
    st.write('you chose: ', option)
    
    for pokemon in info2.pokemonlist:
        if option in pokemon[2]:
            newlist.append(pokemon)
    return(newlist)
            
    st.write('---')
type_section()

def multitype():
    #new
    on = st.toggle('Restrict to single type')
    
    if on:
        st.write("You will only see single type Pokemon")

        for pokemon in newlist:
            if len(pokemon[2]) == 1:
                newlist2.append(pokemon)
        global typefinal
        typefinal = newlist2
        return(typefinal)
        st.write("You will only see single type Pokemon")
    else:
        st.write("Pokemon may have multiple types")
        typefinal=newlist
        return(typefinal)
        st.write("Pokemon may have multiple types")
    st.write('---')

multitype()

def moreinfo_section():
    st.sidebar.header("More Information")
    st.sidebar.text("Look up your Pokemon")
    bulbapedia_link=(f'<a href="{info2.bulbapedia_link}"><img src="{info2.bulbapedia_image}" alt="Bulbapedia" width = "75" height = "75"></a>')
    st.sidebar.markdown(bulbapedia_link, unsafe_allow_html=True)
    st.sidebar.text("Official Pokedex")
    pokedex_link=(f'<a href="{info2.pokedex_link}"><img src="{info2.dex_image}" alt="Pokedex" width = "75" height = "75"></a>')
    st.sidebar.markdown(pokedex_link, unsafe_allow_html=True)
moreinfo_section()

def weight_range():
    st.write('---')
    if len(typefinal) != 0:
        newlist.sort()
        minimum = int(typefinal[0][0])
        maximum = int(typefinal[-1][0])
        #new
        weightrange = st.slider(
            '⚖️Select a weight range',
            minimum , maximum , (minimum , maximum))
        st.write("you are looking at weights from {} to {}".format(weightrange[0],weightrange[1]))
        
        for pokemon in typefinal:
            if int(pokemon[0]) in range(weightrange[0],weightrange[1]):
                newlist3.append(pokemon)
        global final
        final = newlist3
        return(final)
    else:
        st.write("⛔Nothing Pokemon like this exist! Try something else.")
        
        final = newlist3
        return(final)
weight_range()

def chart():
    labels = 'Your Pokemon', 'Other Pokemon'
    sizes=[len(final)/151, ((151-len(final))/151)]
    explode = (.1, 0)

    figure, axis = plt.subplots()
    axis.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    axis.axis('equal')
    st.pyplot(figure)
    
chart() 

def results():
    st.write('---')
    if len(final) == 0:
        st.write("⛔There are not Pokemon Fitting these selections! Try Something else.")
    else:
        st.write("The pokemon that fit your description are listed below. Click their name to learn more!" + "\n")
        for pokemon in final:
            pokeurl = "https://www.pokemon.com/us/pokedex/" + pokemon[1]
            if len(pokemon[2])>1:
                st.write((str([pokemon[1]]) + "({link})" + " a " + pokemon[2][0] + " and " + pokemon[2][1] + " type").format(link=pokeurl)) 
            else:
                st.write((str([pokemon[1]]) + "({link})" + ' a ' + pokemon[2][0] + " type").format(link=pokeurl))
            
        
        
        
             

results()


