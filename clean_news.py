def clean_text(df):
    # Convert content to lower case
    df['content'] = df['content'].str.lower()

    # List of phrases to remove
    phrases_to_remove = [
        'cnn’s.*?\.',
        '© 2023 cable news network. a warner bros. discovery company. all rights reserved.  cnn sans ™ & © 2016 cable news network.',
        'fear & greed index.*?\.',
        'latest market news.*?\.',
        'most stock quote data provided by bats. us market indices are shown in real time, except for the s&p 500 which is refreshed every two minutes. all times are et. factset: factset research systems inc. all rights reserved. chicago mercantile: certain market data is the property of chicago mercantile exchange inc. and its licensors. all rights reserved. dow jones: the dow jones branded indices are proprietary to and are calculated, distributed and marketed by dji opco, a subsidiary of s&p dow jones indices llc and have been licensed for use to s&p opco, llc and cnn. standard & poor’s and s&p are registered trademarks of standard & poor’s financial services llc and dow jones is a registered trademark of dow jones trademark holdings llc. all content of the dow jones branded indices copyright s&p dow jones indices llc and/or its affiliates. fair value provided by indexarb.com. market holidays and trading hours provided by copp clark limited.',
        '–correction:.*?\.',
        'fox.*?\.', 'cnn.*?\.', 'msnbc.*?\.', 'breitbart.*?\.',
        '© 2023 nbc universal',
        'featured shows.*?\.', 'msnbc tv.*?\.', 'more.*?\.', 'follow msnbc.*?\.', 'more brands.*?\.', 'more shows.*?\.',
        'this material may not be published, broadcast, rewritten,or redistributed. ©2023 fox news network, llc. all rights reserved. quotes displayed in real-time or delayed by at least 15 minutes. market data provided by factset. powered and implemented by factset digital solutions. legal statement. mutual fund and etf data provided by refinitiv lipper.',
        'subscribe.*?\.',
        'follow.*?\.', 'click here.*?\.',
        '^write to him at.*$', 'is a reporter for  write to him at.*$',
        'for more of my tips, subscribe to my free cyberguy report newsletter by heading to cyberguy.com/newsletter   2023 cyberguy.com.  all rights reserved.'
    ]
    
    # Apply each phrase removal
    for phrase in phrases_to_remove:
        df['content'] = df['content'].str.replace(phrase, '', regex=True)
        
    # Remove authors' names
    authors = df['author'].str.split(',').str[0].unique()
    for author in authors:
        df['content'] = df['content'].str.replace(str(author), '', regex=True)

    # Remove duplicate titles
    df = df.drop_duplicates(subset=['title'], keep='first')

    return df
