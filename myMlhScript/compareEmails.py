# sfile - csv file of emails already sent to
sfile = open("sents.csv", 'r');
sents = list();
for line in sfile:
    line = line.strip('\n');
    line = line.replace(',', '');
    line = line.replace('"', '');
    sents.append(line);

# nfile - csv file of new registrants
nfile = open('news.csv', 'r')
news = list();
for line in nfile:
    line = line.strip('\n');
    news.append(line);

# create list of new registrants to whom emails have not been sent
tosend = list();
for item in news:
    if item not in sents:
        tosend.append(item);

# write all email addresses that need acceptance letter sent to file
outfile = open('outfile.csv', 'w')
for item in tosend:
    outfile.write(item + ',\n');
#compare two lists and remove duplicates
#print(sents)
#print(news)
#print(set(news + sents));
