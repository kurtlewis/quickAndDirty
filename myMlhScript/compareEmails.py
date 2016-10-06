sfile = open("sents.csv", 'r');
sents = list();
for line in sfile:
    line = line.strip('\n');
    line = line.replace(',', '');
    line = line.replace('"', '');
    sents.append(line);

nfile = open('news.csv', 'r')
news = list();
for line in nfile:
    line = line.strip('\n');
    news.append(line);

tosend = list();
for item in news:
    if item not in sents:
        tosend.append(item);

outfile = open('outfile.csv', 'w')
for item in tosend:
    outfile.write(item + ',\n');
#compare two lists and remove duplicates
#print(sents)
#print(news)
#print(set(news + sents));
