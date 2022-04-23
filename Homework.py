import random
# First of all to use regular Expressions we need to import the modul
# of regular expressions like this:
import re


class SimpleEliza:

    # Eliza's 'intelligence'
    def run(self, input_sent):

        welcome = "Hallo. Worüber möchten Sie mit mir reden?"
        goodbye = "Auf Wiedersehen"
        feelings = ["ängstlich", "bedrückt", "einsam", "erfreut", "gestresst", "glücklich", "traurig", "unzufrieden"]
        dummy_sentences = [
            "Erzählen Sie mir mehr davon.",
            "Interessant.",
            "Können Sie das noch etwas genauer erklären?",
            "Was denken Sie darüber?"
        ]

        # Process user input. Processing continues until the user says goodbye.
        s = input_sent

        if s == goodbye:
            return goodbye

        answer = ""

        # Check for feelings
        for feeling in feelings:

            if feeling in s:
                # Found feeling -> generate answer

                answer = "Why are you feeling " + feeling + "?"

                # stop processing user input
                return answer

        # TODO: Check for family members
        # Create a list of the family members, so it can be used as a
        # variable in the regular Expression.

        family_members = ["Vater", "Mutter" , "Schwester", "Bruder",
                          "Onkel", "Tante", "Cousine", "Cousin",
                          "Opa", "Oma"]

        # now we have to test if one of the family members is actually
        # in the input that was given

        # For this we have to create a regular expression first.
        # We create a blank regular expression to use it in
        # our for loop, to replace it with each family member
        # in our list
        reg_exp_family_member = ""


        for family_member in family_members:

            # Here is the replacement of the family member with the
            # regular expression
            reg_exp = family_member

            # To get all the partial results of the input, and if some
            # family member was mentioned, we need to compile our
            # regular expression first with the re.compile(reg_exp)
            # method and then search the family member in our s input
            # with the .findall(s) method

            # We will combine those two methods into one and will name the
            # variable family_member_suchtreffer

            family_member_suchtreffer = re.compile(reg_exp).findall(s)

            # Now we just have to print those search results with an
            # enumerated for loop

            for treffer in family_member_suchtreffer:
                print(f"Wie geht es {reg_exp}?")




        # TODO: Check for negations
        # To check for negations we first have to know, what a negation
        # looks like in the german language
        # The negation in the german language is defined as followed:
        # "nicht" and every combination of "kein/e/er/es/em/en"
        # So if any of these are mentioned, we know that it is a
        # negation

        # The question is now: How do we put this in a regular expression?
        # One possibility is to use kein|nicht distinction
        # So we just have to make a difference between kein/e/er/es/em/en
        # To do this we can use [Kk]ein[e]*[srms]* as a regular expression
        # The [Kk] is because we don't Know if it is in the beginning
        # of a sentence and the star operator is used, so we don't
        # have to use the other grammatik uses of kein

        # Our regular expression looks like this:
        reg_exp_negation = "[Nn]icht|[Kk]ein[e]*[srms]*"

        # Now we basically do the same like in the family member task
        # 1) Compile and find the results of all the negation:
        negation_search_result = re.compile(reg_exp_negation).findall(s)

        # 2) Print the negations, that have been used and ask them,
        # why they used the negation.
        for treffer in negation_search_result:
            print(f"Warum haben Sie die Verneinung '{treffer}' benutzt?")

        # TODO: distinguish between and & or
        # Basically we will do the same like in the task before with a
        # distinction between "und|oder" in the regular expression
        # The only difference is, that for whether we found an "und"
        # or an "oder", our print result will have to differentiate
        # We have to algorithms to do this
        # a) We could use a regular expression with "[Uu]nd|[Oo]der"
        # b) or we could use two seperate regular expressions and print
        # the results

        # We will choose a)
        # 1) Create the regular expression
        reg_exp_or_and = "[Uu]nd|[Oo]der"

        #2) compile and search for hits
        and_or_searchresult = re.compile(reg_exp_or_and).findall(s)

        #3) print those search hits and distinguish between "oder" and "und"
        for treffer in and_or_searchresult:
            # If the result is "und" or with and Capital letter "Und"
            # it should print out, why we used it in our sentence
            if treffer == "und" or "Und":
                print(f"Warum haben Sie hier {treffer} im Satz benutzt?")
            else:
                print(f"Warum haben Sie hier {treffer} im Satz benutzt?")

        # TODO: ability of your choice

        # output random sentence
        answer = random.choice(dummy_sentences)
        return answer


elize = SimpleEliza()
elize.run("Wie geht es Vater. Und Mutter? Oder ")


