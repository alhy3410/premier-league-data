"""Scrapes premierleague.com for data"""
import re
import sys
import locale
import logging
import requests
from bs4 import BeautifulSoup

locale.setlocale(locale.LC_ALL, 'English_United States.1252')

logging.basicConfig(
    format='%(asctime)s|%(levelname)s|%(message)s',
    level=logging.INFO
)


def get_stats_for_match(match_url):
    """
    Given a match stat url, from premierleague.com,
    returns a stats dict with all match statistics
    """
    soup = BeautifulSoup(requests.get(match_url).text, 'lxml')
    seas = match_url.split('/')[-3]

    # get managers info
    mgrs = [
        soup.select('div .teamtitle .homecol')[0].find_all('a')[-1],
        soup.select('div .teamtitle .awaycol')[0].find_all('a')[-1]
    ]

    match_stat_url = match_url.replace('match-report.html', 'match-stats.html')

    soup = BeautifulSoup(requests.get(match_stat_url).text, 'lxml')

    # get fixture infos
    fis = soup.find('p', 'fixtureinfo').get_text().split('|')
    fis = [re.sub(r'Referee: |Attendance ', '', i).strip() for i in fis]

    # convert attendance to integer
    fis[-1] = locale.atoi(fis[-1])

    # add to stats
    stats = dict(zip(['date', 'venue', 'referee', 'attendance'], fis))
    stats['season'] = seas
    stats['home_manager'] = mgrs[0].get_text().strip()
    stats['away_manager'] = mgrs[1].get_text().strip()

    # get home, away and goals
    css_classes = ['home', 'away', 'countscore']
    res = [soup.find('td', c).get_text().strip() for c in css_classes]

    stats['home_team'], stats['away_team'] = res[0], res[1]
    stats['result'] = res[2].replace(' ', '')

    for loc in ['home', 'away']:
        goals = soup.find('span', '%sScore' % loc).get_text().strip()
        goals_details = [
            li.get_text().strip()
            for li in soup.find('div', '%s goals' % loc).find_all('li')
        ]
        stats['%s_goals' % loc] = locale.atoi(goals)
        stats['%s_goals_details' % loc] = ','.join(goals_details)

    # in depth stats table
    tables = soup.find_all('div', 'statsTable')
    for table in tables:
        t = table.find('table')
        h = t.select('thead th')[1:]
        d = [r.select('td') for r in t.select('tbody tr')]
        for i in zip(h, *d):
            metric = i[0].get_text().strip().lower().replace(' ', '_')
            stats['%s_home_team' % metric] = locale.atoi(i[1].get_text().strip())
            stats['%s_away_team' % metric] = locale.atoi(i[2].get_text().strip())

    return stats


if __name__ == '__main__':
    import pandas as pd
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Path to input file with links', required=True)
    parser.add_argument('-o', '--output', help='Path to save output file', required=True)
    args = parser.parse_args()

    with open(args.input, 'r') as links:
        links = links.readlines()
        tot, data = len(links), []
        for i, link in enumerate(links):
            url = '%s%s' % ('http://www.premierleague.com', link.strip())
            data.append(get_stats_for_match(url))
            logging.info('#(%d/%d) Completed crawl for %s' % (i + 1, tot, url.split('/')[-1]))

    pd.DataFrame(data).to_csv(args.output, index=False, encoding='utf-8')
