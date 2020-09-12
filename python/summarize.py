from gensim.summarization import summarize
from gensim.summarization import keywords

SUMMARY_SIZE = 80

def getSummary(newsList):
    updatedList = []
    for news in newsList:
        ratio = len(news["body"].split(" "))
        ratio = (float)(SUMMARY_SIZE/ratio)
        if ratio >= 1:
            ratio = 1
        news["body"] = summarize(news["body"], ratio)
        ratio = 0.25
        news["keywords"] = keywords(news["body"], ratio)
        updatedList.append(news)
    return updatedList


if __name__ == "__main__":
    article = """Reliance Industries' (RIL) plan to sell a stake in its retail subsidiary at an equity valuation of Rs 4.21 lakh crore and its proposed acquisition of Future Group's retail businesses will solidify its position in India's organised retail market and strengthen its consumer business, says Fitch Ratings. It also expects the synergies from the acquisition to enhance RIL's bargaining power with vendors, and offline and online customer reach. The global research firm believes that the proposed acquisition of Future Group's retail business will fortify its retail footprint, especially in the grocery retail sub-segment. Last month, RIL acquired the retail business of Kishore Biyani-led Future Group for Rs 24,713 crore. Earlier this week, American private equity firm Silver Lake announced an investment of Rs 7,500 crore ($1 billion) in Reliance Retail Ltd, a Reliance Industries Ltd subsidiary, for a 1.75 per cent equity stake on a fully diluted basis. As per reports, US-based PE investors KKR and Co., Mubadala Investment Co., and Abu Dhabi Investment Authority (ADIA) are also in talk to invest in retail arm of Reliance Industries. According to Fitch, the equity stake sale will further strengthen RIL's financial profile and competitive position beyond the proposed acquisition. On Future Retail's acquisition, the research firm said that it will add about 1,700 large stores to RIL's 11,806 stores in its retail segment and increase its organised retail revenue market share by around 5 per cent. The asset acquisition will add about 2-2.5 per cent to RIL's EBITDA for the financial year 2021-2022 (FY22). "The Rs 24,700 crore ($3.4 billion) consideration for the acquisition is less than 3 per cent of its FY20 total assets, a relatively small impact on its balance sheet," Fitch said. Future Group's solid presence in Tier 1 Indian cities with well-established retail formats, including Big Bazaar, Central, FBB, Easyday and Brand Factory, will complement RIL's increasing strength in second- and third-tier cities. RIL's acquisition of Future Group's warehousing and logistics business, in addition to its stores, will help to expand the scale of JioMart, RIL's online grocery platform, the agency said. The Future Group asset acquisition is subject to regulatory, shareholder, creditor and other customary approvals, which may take around six months to complete. The total consideration of Rs 24,700 crore would include a cash payment of about Rs 5,000-6,000 crore and balance as liabilities would be absorbed by RIL, Fitch said. "We retain our expectations for RIL to return to a net cash position by FY22, despite the additional debt for the transaction" it said. Fitch said that its net cash expectation is driven by proceeds from the sale of RIL's stakes in its telecom and retail subsidiaries. RIL has announced plans to sell a 1.75 per cent stake in Reliance Retail Ventures Limited, its retail subsidiary, to Silver Lake for Rs 7,500 crore, subject to regulatory and other customary approvals. This is in addition to the sale of around 33 per cent of Jio Platforms for Rs 1.52 lakh crore. RIL has also completed its Rs 53,100 crore rights issue in June 2020, with Rs 13,300 crore in cash received to date and the balance in FY22. RIL's net cash position would also be helped by the completion of a Rs 25,200 investment by Canada's Brookfield Infrastructure Partners LP in Tower Infrastructure Trust, which plans to use part of the proceeds to pay down RIL's investment (Rs 12,800 crore as of March 2020) in the non-convertible debentures issued by the trust. In addition, RIL received Rs 7,600 crore in Q1 FY21 from BP plc for a 49 per cent stake in RIL's fuel retail network and aviation fuel business. """
    article_summary = summarize(article, ratio=0.2)
    print(article)
    print("Summary: ")
    print(article_summary)
    print("keywords: ")
    print(keywords(article_summary, ratio=0.5))