/***
Lists all fixtures / match links from premierleague.com
*/
var fs      = require('fs'),
    casper  = require('casper').create();

var url 	= 'http://www.premierleague.com/en-gb/matchday/results.html',
	links 	= [];

casper.start(url, function() {
    links = this.getElementsAttribute('.contentTable td.clubs.score a', 'href');
});

casper.then(function () {
    this.echo('Links:')
    this.each(links, function(casper, link, i) {
        this.echo(link);
    });
});

casper.run();
