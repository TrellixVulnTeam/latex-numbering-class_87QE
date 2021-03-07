import streamlit as st

from latex_equation_numbering import latex_equation_numbering


# Instantiate the latex_equation_numbering class
equations = latex_equation_numbering()

equations_numbers_styled = latex_equation_numbering(display_inline_number_style=('italic', 'bold'))

def main():

    st.title('Testing the `latex_equation_numbering` class')

    st.header('Plain style for numbers')

    st.write(
        '''
            Here is our first equation:
        '''
    )
    equations.add_equation('pythagoras', r'a^2 + b^2 = c^2', numbered=True)
    equations.display_equation('pythagoras')
    st.write(
        f'''
            As we see in Eq. ({equations.eqref('pythagoras', linked=True)}) we have a labeled and centered equation with a hyperlinked inline citation! Now here is an unlabeled equation:
        ''', unsafe_allow_html=True
    )
    equations.add_equation('einstein', r'E = mc^2', numbered=False)
    equations.display_equation('einstein')
    st.write(
        '''
            And another numbered equation:
        '''
    )
    equations.add_equation('quadratic', r'x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}', numbered=True)
    equations.display_equation('quadratic')
    st.write(
        f'''
            Now we have three equations, two numbered ones: Eqs. ({equations.eqref('pythagoras', linked=False)}) and Eq. ({equations.eqref('quadratic', linked=True)}), and one unnumbered equation. Notice how the numbering is updated, and we can turn off the hyperlinking if we wish!

            Now lets add some line breaks to really test out the inline equation links: {''.join('<br>' for i in range(50))}

            

            Eqs. ({equations.eqref('pythagoras', linked=True)}) and Eq. ({equations.eqref('quadratic', linked=True)})
        ''', unsafe_allow_html=True
    )

    st.header('Italic display equation numbers and bold inline equation numbers')

    st.write(
        '''
            Here is our first equation:
        '''
    )
    equations_numbers_styled.add_equation('pythagoras', r'a^2 + b^2 = c^2', numbered=True)
    equations_numbers_styled.display_equation('pythagoras')
    st.write(
        f'''
            As we see in Eq. ({equations_numbers_styled.eqref('pythagoras', linked=True)}) we have a labeled and centered equation with a hyperlinked inline citation! Now here is an unlabeled equation:
        ''', unsafe_allow_html=True
    )
    equations_numbers_styled.add_equation('einstein', r'E = mc^2', numbered=False)
    equations_numbers_styled.display_equation('einstein')
    st.write(
        '''
            And another numbered equation:
        '''
    )
    equations_numbers_styled.add_equation('quadratic', r'x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}', numbered=True)
    equations_numbers_styled.display_equation('quadratic')
    st.write(
        f'''
            Now we have three equations, two numbered ones: Eqs. ({equations_numbers_styled.eqref('pythagoras', linked=False)}) and Eq. ({equations_numbers_styled.eqref('quadratic', linked=True)}), and one unnumbered equation. Notice how the numbering is updated, and we can turn off the hyperlinking if we wish!

            Now lets add some line breaks to really test out the inline equation links: {''.join('<br>' for i in range(50))}

            

            Eqs. ({equations_numbers_styled.eqref('pythagoras', linked=True)}) and Eq. ({equations_numbers_styled.eqref('quadratic', linked=True)})
        ''', unsafe_allow_html=True
    )

# Run main function
if __name__ == "__main__":
    main()