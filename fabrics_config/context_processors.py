from fabrics_main.models import MenuCategoriy, Caregoriy






def dropdownmenu(request):
    m_categoriy = MenuCategoriy.objects.filter()
    categori = Caregoriy.objects.filter(parent=None, menucategoriy_id=2)
    print("ASDFGHJKJTREWQWERTYU-------------__?>>>>>>>>>>.", categori)
    return {
        'm_categoriy': m_categoriy,
        'categori': categori
    }