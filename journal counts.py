import json
with open("OpenAlex_BusinessEnglish_070722.json", "r") as f:
    dat = json.load(f)
    #print(dat)
author_count = dict()
for item in dat:
    journal = item.get("host_venue", {}).get("display_name",None)

    if journal is None:
        continue
    else:
              if journal in author_count:
                  author_count[journal] += 1
              else:
                  author_count[journal] = 1

    count=sorted(author_count.items(), key=lambda x: x[1], reverse=True)

    print(count)







