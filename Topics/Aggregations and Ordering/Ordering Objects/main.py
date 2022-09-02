elm_street_houses = House.objects.filter(street="Elm st.").order_by('house_number')
