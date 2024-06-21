
import utils


def main():
    # Load environment variables
    utils.load_environment_variables()
    
    # Initialize OpenAI API
    utils.initialize_openai_api()
    
    # Create the LangChain chain
    chain = utils.create_chain()
    
    # Define the reviews
    dress_reviews = [
        "I had such high hopes for this dress and really wanted it to work for me. i initially ordered the petite small (my usual size) but i found this to be outrageously small. so small in fact that i could not zip it up! i reordered it in petite medium, which was just ok. overall, the top half was comfortable and fit nicely, but the bottom half had a very tight under layer and several somewhat cheap (net) over layers. imo, a major design flaw was the net over layer sewn directly into the zipper - it c",
        "I'm 5ft 5in and 125 lbs. i ordered the s petite to make sure the length wasn't too long. i typically wear an xs regular in retailer dresses. if you're less busty (34b cup or smaller), a s petite will fit you perfectly (snug, but not tight). i love that i could dress it up for a party, or down for work. i love that the tulle is longer then the fabric underneath.",
        "This H&M Dress runs small esp where the zipper area runs. i ordered the sp which typically fits me and it was very tight! the material on the top looks and feels very cheap that even just pulling on it will cause it to rip the fabric. pretty disappointed as it was going to be my christmas dress this year! needless to say it will be going back.",
        "I love the look and feel of this tulle dress. i was looking for something different, but not over the top for new year's eve. i'm small chested and the top of this dress is form fitting for a flattering look. once i steamed the tulle, it was perfect! i ordered an xsp. length was perfect too.",
        "I was hesitant based on the reviews, but i'm glad i ordered this H&M dress (in blue). the material is like a french dot texture that is soft but still a bit structured. i had no issues with the fit. it's appropriately just a little oversized. the styling is very mod!",
        "I found this dress delightful! i have worn it numerous times and though quite long (for some girls) fits me well. my only complaint is that if the wind blows it tends to fly open as there is only on clasp at the breast. the fabric is light and comfortable, i wore it in costa rica and it felt refreshing. i am 5ft 9in, 155 lbs and a 34a cup; i would suggest a larger size for girls as the small fit me very well.",
        "Three strikes and retailer is out for me! i am so disappointed. i really liked this dress and was looking for a fun, distinctive new shift dress. got it, tried it on, took it off, went back to look at the listing online...nowhere does it mention that it has a drop-seam in the shoulders. i guess you can see it if you zoom in closely on the image, but it's not mentioned in the text. who on god's green earth actually looks good with a drop-shoulder?! it hits every woman under 5ft 10in right in the middl",
        "This is such a unique and fun dress. i'm so glad i found it and it fits perfectly! I always search each summer for a maxi dress and this is the winner this summed! i love the way it wraps. fits perfectly. I got a size medium and i am 5ft 5in 34dd Beautiful H&M Dress",
        "This is a nice choice for holiday gatherings. i like that the length grazes the knee so it is conservative enough for office related gatherings. the size small fit me well - i am usually a size 2/4 with a small bust. in my opinion it runs small and those with larger busts will definitely have to size up (but then perhaps the waist will be too big). the problem with this dress is the quality. the fabrics are terrible. the delicate netting type fabric on the top layer of skirt got stuck in the zip",
        "First of all, this is not pullover styling. there is a side zipper. i wouldn't have purchased it if i knew there was a side zipper because i have a large bust and side zippers are next to impossible for me. second of all, the tulle feels and looks cheap and the slip has an awkward tight shape underneath. not at all what is looks like or is described as. sadly will be returning, but i'm sure i will find something to exchange it for!"
    ]
    
    # Process the reviews
    results = utils.process_reviews(chain, dress_reviews)
    
    # Print the results
    print(results)

if __name__ == "__main__":
    main()