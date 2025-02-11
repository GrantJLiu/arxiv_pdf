import arxiv as arxiv
import csv


QUERY = "AI"
SEARCHDATE = "202502011200"
SEARCHDATE2 = "202502081200"
FILENAME = "test.csv"



def main():
    client = arxiv.Client()
    search = arxiv.Search(
        query = QUERY + " submittedDate:[202502081200 TO 202502091200]",
        sort_by = arxiv.SortCriterion.Relevance,
        sort_order = arxiv.SortOrder.Descending,
        max_results = 10 
    )
    results = client.results(search)
    header = ["Title", "Authors", "Abstract", "Primary Category", "Categories", "URL"]
    file = open(FILENAME, "w", newline = "", encoding="utf-8")
    with file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        for r in results:
            writer.writerow({
                "Title" : r.title,
                "Authors" : r.authors,
                "Abstract" : r.summary,
                "Primary Category" : r.primary_category,
                "Categories" : r.categories,
                "URL" : r
            })
            #r.download_pdf()
    file.close()
if __name__ == "__main__":
    main()