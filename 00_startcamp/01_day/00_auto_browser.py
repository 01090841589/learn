import webbrowser

menu = "햄버거", "치킨", "짜장면", "밥"
for i in menu :
    webbrowser.open_new_tab('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query={0}'.format(i))