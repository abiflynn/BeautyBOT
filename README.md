# BeautyBOT

[BeautyBOT](https://abiflynn-beautybot--streamlitbeautybot-e4dh3u.streamlit.app/) is a brand neutral beauty interface I have created to provide unbiased recommendations to consumers, helping them navigate the overwhelming number of choices in the beauty industry. BeautyBOT works across the three key areas of the beauty industry.

1. Fragrance
2. Makeup
3. Skincare

## How does BeautyBOT do?

BeautyBOT uses unsupervised machine learning; K-Means clustering algorithm and encoding to analyse the features of a user's inputted product and recommends new products based on the similarity of these features, such as base notes, ingredients, or saturation.

## Why is there a need for BeautyBOT?

The beauty industry is the fastest growing non-food retail sector and is predicted to continue growing strongly, +17% to 2027.

<img width="528" alt="Screenshot 2023-03-30 at 10 24 29" src="https://user-images.githubusercontent.com/120720780/233968445-0f3dff73-a74d-46df-b533-f7d7f8c35478.png">

Due to the strong predicted growth of the beauty industry non-specialist retailers are now also entering the market and it is therefore becoming highly saturated.

**70%** of beauty consumers are overwhelmed by too many beauty product choices.

With the rise of online shopping, accelerated by the COVID-19 pandemic, and the growing demand for personalisation, consumers are becoming increasingly demanding and expecting immediate results. Also driven by the success seen in other industries, such as with Netflix and Spotify. BeautyBOT aims to meet these expectations by providing instant recommendations that are tailored to each individual user.

As the beauty industry continues to grow, it is clear that retailers need to turn to technology to set themselves apart and provide more personalised experiences for their customers.

BeautyBOT is at the forefront of this trend, offering a solution that provides customers with detailed recommendations from across all brands and products, without the need to download multiple apps, essentially becoming the Netflix of beauty.

Companies that can provide the most innovative and personalised experiences for their customers will be the ones that succeed. A brand-neutral interface, such as BeautyBOT, that offers unlimited recommendations, will help retailers drive growth, increase sales, profits, and customer loyalty.

## BeautyBOT: Recommenders

### Fragrance 
- Input your gender and BeautyBOT will generate the top 5 male/female fragrances based on user ratings.
- Input your favourite fragrance and BeautyBOT will recommend you fragrances based on the scent, base notes, and middle notes.

### Skincare
- Input your favourite skincare product and BeautyBOT will recommend you products of the same product type based on the ingredients.
- BeautyBOT will also recommend you products from different product types based on the ingredients.

### Make-up
- Input your favourite foundation product and shade and BeautyBOT will recommend you other foundations based on the hue, saturation, and lightness.

## Streamlit App 

I have created a streamlit app for users to use these recommenders. [Link Here!](https://abiflynn-beautybot--streamlitbeautybot-e4dh3u.streamlit.app/)


## Constraints 

As with any recommendation system the lack of comprehensive data was a major limitation of this project. Without user data it is hard to understand user preferences, behaviours, and demographics, the system is therefore unable to make accurate and personalised recommendations. Additionally, using a limited dataset can also limit the input options available for users, which can negatively impact the customer experience.

### Consumer Facing Limitations:
User inputs must be written the same as they appear in the dataset, including spelling, grammar, symbols, and capitalisation.
Recommenders will only work for brands/products/shades that are included in the datasets that were available. Meaning certain brands and products will be unavailable to the consumers.

### Data Limitations:
- User to User Data: Reviews, rankings, and ratings.
- Sales Data: Current most popular products by sales.
- New Releases: Newest products on the market.
- User Shopping Habits: Previous purchases, clicks and products viewed.
- Product Information: Missing information price, gender, and size.

### Quantifying Results:
As with any unsupervised machine learning another limitation is the ability to quantitatively measure the accuracy of the results. However, I have conducted a comprehensive qualitative analysis and found the results to be conclusive and sensible.

## Future Capabilities

If these limitations were not a factor, the project could evolve to include data on user demographics, behaviours, preferences, and past interactions, allowing for a more personalised and effective approach to recommendations. As well as this with access to sales and market data this interface would be able to include recommendations based on sales, new releases, and market trends. With a bigger dataset including more brands and products the blue-sky future of BeautyBOT is to become the **Netflix of Beauty**.





