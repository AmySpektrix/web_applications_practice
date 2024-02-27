from playwright.sync_api import Page, expect

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f'http://{test_web_address}/albums')
    div_tags = page.locator('div')
    expect(div_tags).to_have_text([
        '\n Title: Doolittle, Released: 1989 \n',
        '\n Title: Surfer Rosa, Released: 1988 \n',
        '\n Title: Waterloo, Released: 1974 \n',
        '\n Title: Super Trouper, Released: 1980 \n',
        '\n Title: Bossanova, Released: 1990 \n',
        '\n Title: Lover, Released: 2019 \n',
        '\n Title: Folklore, Released: 2020 \n',
        '\n Title: I Put a Spell on You, Released: 1965 \n',                
        '\n Title: Baltimore, Released: 1978 \n',
    ])

def test_get_album(page, test_web_address,db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f'http://{test_web_address}/albums/1')
    expect(page.locator('h1')).to_have_text('\n Doolittle \n',)
    expect(page.locator('p')).to_have_text('\n Release year: 1989 \n Artist: Pixies \n',)

def test_albums_links(page, test_web_address,db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f'http://{test_web_address}/albums')
    page.click ('text="Title: Doolittle"')
    expect(page).to_have_url(f'http://{test_web_address}/albums/1')
    page.goto(f'http://{test_web_address}/albums')
    page.click ('text="Title: Surfer Rosa"')
    expect(page).to_have_url(f'http://{test_web_address}/albums/2')    

def test_get_artist(page, test_web_address,db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f'http://{test_web_address}/artists/1')
    expect(page.locator('h1')).to_have_text('\n 1 - Pixies \n',)
    expect(page.locator('p')).to_have_text('\n Genre: Rock \n',)

def test_get_artists(page,test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f'http://{test_web_address}/artists')
    div_tags = page.locator('div')
    expect(div_tags).to_have_text([
        '\n 1 - Pixies \n',
        '\n 2 - ABBA \n',
        '\n 3 - Taylor Swift \n',
        '\n 4 - Nina Simone \n',])

def test_artists_link(page,test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f'http://{test_web_address}/artists')
    page.click ('text="1 - Pixies"')
    expect (page).to_have_url(f'http://{test_web_address}/artists/1')
    page.goto(f'http://{test_web_address}/artists')
    page.click ('text="2 - ABBA"')
    expect (page).to_have_url(f'http://{test_web_address}/artists/2')

"""
when we click 'create new album' and add valid information it creates a new album and moves to new page for that album
"""
def test_add_album(page,test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f'http://{test_web_address}/albums')
    page.click ("text='Add new album'")
    page.fill("input[name=album_title]", "Test Album")
    page.fill("input[name=release_year]", "1975")
    page.select_option("[name=artist_name]", "Pixies")
    page.click('input[value="Create Album"]')
    expect(page.locator('h1')).to_have_text('\n Test Album \n',)
    expect(page.locator('p')).to_have_text('\n Release year: 1975 \n Artist: Pixies \n',)
    page.click('text="Click here to go back to all albums"')
    expect(page.locator('div')).to_have_text([
        '\n Title: Doolittle, Released: 1989 \n',
        '\n Title: Surfer Rosa, Released: 1988 \n',
        '\n Title: Waterloo, Released: 1974 \n',
        '\n Title: Super Trouper, Released: 1980 \n',
        '\n Title: Bossanova, Released: 1990 \n',
        '\n Title: Lover, Released: 2019 \n',
        '\n Title: Folklore, Released: 2020 \n',
        '\n Title: I Put a Spell on You, Released: 1965 \n',                
        '\n Title: Baltimore, Released: 1978 \n',
        '\n Title: Test Album, Released: 1975 \n'
    ])


# """
# When we submit with no information it gives an error
# """
# def test_validate_album(page,test_web_address, db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     page.goto(f'http://{test_web_address}/albums')
#     page.click ("text='Add new album'")
#     page.click('input[value="Create Album"]')
#     errors_tag = page.locator(".t-errors")
#     expect(errors_tag).to_have_text("Your submission contains errors: you are missing album name and release year")