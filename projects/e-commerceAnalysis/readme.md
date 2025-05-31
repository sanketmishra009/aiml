# E-commerce Data Analysis Insights

## Q1. Identify the months with the highest and lowest acquisition rates. What strategies could be implemented to address the fluctuations and ensure consistent growth throughout the year?

### Logic Used:

1. The first transactions are extracted by performing a grouping on each customer and getting the first date they purchased.
2. The resulting dataframe is again grouped by months and aggeregated on transaction counts.

---

### ✅ Insight: Customer Acquisition Rate by Month

**Based on the analysis:**

- 📈 Highest acquisition month: January — 215 new customers

- 📉 Lowest acquisition month: November — 68 new customers

### 🔍 Reason Behind Fluctuations

- January's peak may align with New Year promotions, holiday gift card usage, or seasonal marketing.

- November's low may reflect pre-holiday shopping hesitation, or competitive discounting elsewhere pulling traffic away.

---

### ✅ Recommended Strategies for Consistent Growth

- Replicate January’s successful campaigns:

  - Analyze offers, creatives, channels, and audience segments used.

  - Use similar promotions in low-performing months (e.g., November, September).

- Mid-year engagement push:

  - Run flash sales, influencer campaigns, or loyalty point multipliers in May–July to sustain mid-year growth.

- Personalized re-targeting:

  - Use lookalike audiences based on high-LTV customers from January to drive new acquisition.

- Pre-holiday teaser events:

  - In October/November, use early-bird Black Friday access or “mystery discounts” to prevent the dip seen in November.

- Referral programs:

  - Encourage current customers to bring in new ones during off-peak months with tiered rewards.

- Content-driven acquisition:

  - Run seasonal buying guides, blogs, or webinars to generate organic interest in slow months.

- Influencer & partnership leverage:

  - Use micro-influencers in off-peak periods to promote limited-time acquisition discounts.

## Q2. Analyze the data to determine if certain months consistently show higher or lower acquisition rates. How can the company capitalize on high-performing months and improve performance during slower periods?

![alt text](images/q2.png)

### Logic Used:

-Simply plot the data.

---

### **🔍 Insights: High vs Low Consistency:**

### ✅ Consistently High-Performing Months

- January (highest): post-holiday engagement, New Year campaigns.

- March–April: likely driven by spring promotions.

- July: mid-year spike, possibly clearance or back-to-school prep.

### 🚫 Consistently Low-Performing Months

- September & November: possibly due to:

  - Minimal promotions

  - Holiday budget saving

  - Market competition

---

### ✅ Strategies to Capitalize on Trends

- For High-Performing Months:

  - Audit and Reuse Campaigns

  - Analyze creatives, offers, and timing that worked in Jan/March.

  - Replicate strategies with minor tweaks in low-performing months.

  - Expand Budget Allocation

  - Allocate more marketing spend to high-performing months to amplify ROI.

  - Leverage Referrals

  - Introduce referral drives in strong months to extend their tail impact.

- For Low-Performing Months:

  - Launch Pre-Sale Campaigns

  - Run teaser deals in August and October to energize acquisition before Sep/Nov slumps.

  - Personalized Ads

  - Use behavioral retargeting to convert passive shoppers during slow periods.

  - Geo-Targeted Offers

  - Use location-based discounts if certain regions underperform.

  - Experiment with A/B Tests

  - Trial different offers, timings, and creatives to test what works in slower months.

---

### **📌 Final Thought:**

- Capitalizing on high months while strategically improving slower months creates a balanced, sustainable acquisition engine that avoids over-reliance on seasonal spikes.

## Q3. Identify periods with the strongest and weakest retention rates. What strategies could be implemented to improve retention during weaker months?

![alt text](images/q3.png)

### Logic Used:

- The transactions which occur after the first transaction for a customer are counted as repeated transactions.

---

### ✅ Strongest Retention Periods (based on bar chart):

- 1.August (peak retention)

- 2.July, June, December (also strong)

* These months show high retention numbers, supported by prior high acquisitions. Likely contributing factors:

  1.Seasonal campaigns

  2.Mid-year and year-end promotions

  3.Better onboarding during peak months

---

### 🚫 Weakest Retention Periods:

**January & February have the lowest retention, despite steady acquisition**

- Possible reasons:

  - Low post-holiday engagement

  - Weak retention campaigns or delayed follow-up

  - First-time buyers who didn’t find immediate value

---

### 🔁 Retention Strategy Recommendations

- For Weak Months (Jan–Feb):

  - Post-Purchase Nudges:

  * Trigger targeted emails or WhatsApp messages 3–5 days post-purchase with tailored product suggestions.

  - Limited-Time Return Incentives:Offer a discount if the user returns within 10–15 days of their first purchase.

  - Holiday Recovery Campaigns:Run campaigns like "New Year Comeback Deals" to bring back buyers post-holidays.

* For Strong Months (Jun–Aug, Dec):

  - Build Loyalty Triggers:

    - Set up milestone rewards (e.g., “3 orders = free delivery”) to maintain retention momentum.

  - Leverage High-LTV Customers:

    - Use their behavior to create lookalike audiences for targeted ads in weak months.

  - Survey and Feedback Loops:

    - Identify what delighted customers in strong months and replicate messaging/timing.

## Q4. Analyze customer behavior during high-retention months and suggest ways to replicate this success throughout the year.

![alt](./images/q4.png)

### **Logic Used:**

- Calculate monthly retentions.
- Aggregate different statistics from different features to analyse during different retention periods.

---

### **🔍 Analysis: Customer Behavior During High-Retention Months**

**📈 Step 1: Identifying High-Retention Months**

- From your previous retention matrix and data:
  |Month | Retention Count | Observation.|
  |-------|-----------|-|
  |August |Highest(185) |Late Q3 peak, possibly due to campaigns or seasonal reactivation.|
  |July | High(160) | Strong mid-year engagement.|
  |December | High(150) | Holiday season, promotional offers.|
  |October–November | High | End-of-year momentum from festive campaigns.|

---

### **🧠 Step 2: Behavior Patterns in High-Retention Months**

- ✅ Common Trends:

  - High coupon usage (seen in July–December).

  - Increased marketing spend (particularly November–December).

  - Product focus: Categories like Nest-USA, Apparel, and Lifestyle spike during these periods.

  - Delivery tier engagement: Mostly mid-tier delivery, suggesting balance of cost and convenience.

  - Average transaction value holds steady, not significantly discounted—indicating healthy margins.

---

### **🎯 Step 3: Strategies to Replicate High-Retention Success Across the Year**

| Retention Driver             | Strategy to Scale Year-Round.                                                                          |
| ---------------------------- | ------------------------------------------------------------------------------------------------------ |
| 🎁 Effective Coupon Use      | Launch rotating monthly coupons tied to product categories (e.g., electronics in Jan, apparel in Mar). |
| 💬 Marketing Spend ROI       | Reallocate budget from low-ROI months to repeat what works in July–Dec: targeted ads, remarketing.     |
| 🛍️ Category-Driven Retention | Promote seasonal bestsellers outside their core months (e.g., smart home bundles in Q2).               |
| 🚚 Delivery Experience       | Extend mid-tier delivery incentives (e.g., free delivery on orders over ₹X in slow months).            |
| 📆 Customer Milestone Offers | Send personalized offers on customer anniversaries, birthdays, or monthly loyalty streaks.             |
| 🔁 Engagement Hooks          | Use tactics like “2nd Purchase Coupons” and next-purchase incentives in Q1 & Q2.                       |

- 💡 Example Action Plan:

  - Month Campaign Focus Retention Tactic
  - January New Year Essentials (Office, Apparel) Bonus points for 2+ orders
  - April Summer Ready (Drinkware, Bags) Free shipping on 2nd order
  - June Mid-Year Sale Rehearsal Flash coupon + early access preview
  - September Festive Warm-Up (Gift Cards, Lifestyle) Retarget lapsed customers with bundles

---

### **✅ Final Takeaway:**

- High-retention periods thrive on well-timed, personalized, and value-driven engagement.
- By analyzing behavior in July–December, the company can implement smartly timed campaigns, delivery incentives, and product targeting to replicate retention spikes throughout the year.

## Q5. Compare the revenue generated by new and existing customers month-over-month. What does this trend suggest about the balance between acquisition and retention efforts?

![alt text](./images/q5.png)

![alt](./images/q5.2.png)

### Logic Used:

- Subset the data according to purchase type.

### **🔍 Key Insights:**

- Revenue from Existing Customers contributes a significant share (often >50%) in most months.

- Spikes in “New” customer revenue are observed in early and mid-year months, indicating effective acquisition campaigns.

- Sustained revenue from existing customers suggests strong retention and loyalty behavior.

---

### **🎯 What This Trend Suggests:**

**✅ Positive Signs:**

- Retention is paying off: Existing customers are returning and generating meaningful revenue.

- Balanced customer base: You’re not solely dependent on new acquisitions.

---

### **⚠️ Risks/Opportunities:**

- If new customer revenue dips too low in some months, acquisition efforts may need a boost.

**Consider increasing CLV (Customer Lifetime Value) through:**

- Loyalty programs

- Subscription models

- Upselling / cross-selling

## Q.6 Analyze the relationship between coupon usage and revenue generation. How can discount strategies be optimized to maximize revenue while maintaining profitability?

![q6](./images/q6.png)

### **Logic Used:**

- Group Transactions by coupon status.
- Aggregate based on revenue.

---

### 📊 Observations:

**_"Clicked" Generates the Highest Revenue:_**

- The "Clicked" category contributes the most to overall revenue, exceeding ₹2.3 million.

* This implies that users who interacted with the coupon (e.g. clicked on it) but did not necessarily redeem it still made substantial purchases.

**_"Used" Performs Well but Not the Highest:_**

- The "Used" coupon category contributes around ₹1.55 million in revenue.

- This confirms that coupon redemption does help drive revenue but doesn’t outperform the "Clicked" group.

**_"Not Used" Lags Behind:_**

- The "Not Used" category contributes the least, under ₹750,000.

- Customers who didn’t engage with coupons at all generated significantly less revenue.

---

### 🧠 Interpretation & Strategy Recommendations:

**_Engagement Triggers Revenue:_**

- Simply exposing users to coupons (clicks) appears to influence purchasing behavior positively, even without redemption.

- Optimize placement and visibility of coupons to increase clicks — e.g., homepage banners, cart page offers.

**_Optimize Redemption Strategy:_**

- Since “Used” also brings strong revenue, offer time-limited or personalized coupons to push users from "Clicked" to "Used".

- Add nudges like "You’ve unlocked a 10% discount! Apply now."

**_Educate and Incentivize Non-Users:_**

- Users who didn’t interact with any coupons generated the lowest revenue.

- Target these users with onboarding emails, loyalty programs, or first-order discounts to pull them into the coupon ecosystem.

**_Test Engagement-First Strategies:_**

- A/B test campaigns focused on clicks without heavy discounting, as clicks alone are valuable revenue drivers.

## Q.7 Identify the top-performing products and analyze the factors driving their success.

![q7](./images/q7.png)

### **Logic Used:**

- Group by products.
- Sort in descending manner and display results.

---

### **_The chart above shows the top 10 products by total revenue. Key findings and their implications are:_**

### **_🔝 Top Products by Revenue:_**

- Nest Learning Thermostat 3rd Gen - Stainless Steel

- Nest Cam Outdoor Security Camera

- Nest Cam Indoor Security Camera

- Nest Protect Smoke + CO Alarms (Battery & Wired)

- Nest Secure Alarm System Starter Pack

These products combine high selling price with strong volume demand, making them revenue powerhouses.

---

### **_🔍 Success Factors:_**

- Brand Recognition: Popular Nest-branded products (thermostats, cameras) dominate the list due to trust, quality, and integrated smart home features.

- High Average Unit Price: Products like thermostats and cameras have high price points, increasing per-sale revenue.

- Functional Value & Demand: Security and smart home automation are high-priority categories for customers.

- Cross-Selling Opportunities: These products often complement each other (e.g., thermostat + camera), suggesting bundling may be driving multiple-item purchases.

- Seasonality or Promotions: Some items may have benefited from discounts or marketing pushes (e.g., smart devices in winter or sale seasons).

---

### **_🏪 Inventory Management Recommendations:_**

- Prioritize Stocking: Ensure consistent inventory for the top-selling SKUs to avoid stockouts, especially during peak months.

- Safety Stock Strategy: Maintain buffer stock for high-demand items like thermostats and cameras, using historical monthly sales data.

- Lead Time Optimization: For top sellers, reduce lead time by sourcing them in advance or from faster suppliers.

---

### **_💡 Promotional Strategy Recommendations:_**

- Focus Campaigns on Top SKUs: Allocate more budget to products with high revenue contribution, especially during seasonal demand spikes.

- Bundle Offers: Combine top products (e.g., thermostat + camera) into discounted packages to increase average order value.

- Loyalty Points & Coupons: Incentivize repeat purchases on these categories with loyalty programs or tiered discounts.

- Personalized Marketing: Use customer purchase history to recommend related high-performing products.

## Q.8 Analyze the relationship between monthly marketing spend and revenue. Are there any months where marketing efforts yielded disproportionately high or low returns? How can marketing strategies be adjusted to improve ROI?

![q8](./images/q8.png)

### **Logic Used:**

- Groupby month and aggregate over revenue and marketing spend from transactions and marketing data respectively.

---

### 📊 Marketing Spend vs Revenue Analysis (2019)

### 🔍 Key Observations:

#### Disproportionately High ROI Months:

- July and November stand out with the highest ROI, exceeding 3.0.

- Indicates efficient marketing: modest spend produced high revenue.

- Likely boosted by seasonal campaigns or strong-performing product sales.

#### Disproportionately Low ROI Months:

- February and June show low ROI (near 2.3–2.4).

- These months had comparatively higher spend with lower revenue returns, signaling inefficiency or poor campaign targeting.

- Spending vs Revenue Correlation:

- While total revenue does trend upwards with marketing spend, increased spend doesn't always equate to better returns.

- ROI plateaus or declines when spend increases without strategic optimization.

---

#### 📈 Recommendations to Improve Marketing ROI:

1. Double Down on High-ROI Months:

   - Scale up spend during months like July and November, focusing on already successful channels or campaigns.

   Refine Campaigns in Low-ROI Periods:

   - Audit February and June efforts: was the messaging, targeting, or product offering misaligned?

   - A/B test alternate creatives or shift channel emphasis.

2. Dynamic Budgeting:

   - Move away from flat monthly budgets — allocate based on past ROI trends, forecasted seasonality, and expected product launches.

   Shift Toward Performance Channels:

   - Increase investment in digital channels that allow better tracking and targeting (e.g., Google Ads, social retargeting).

3. Run Attribution Modeling:

   - Identify which channels drive assisted conversions and optimize cross-channel synergy.

4. Tie Marketing to Product Strategy:

   - Promote high-margin or top-performing products during low-ROI months to lift returns without increasing spend.

## Q.9 Evaluate the effectiveness of marketing campaigns by comparing marketing spend to revenue generated. Are there opportunities to reallocate resources for better results?

![q9.1](./images/q9.1.png)

![q9.2](./images/q9.2.png)

### 📈 Effectiveness of Marketing Campaigns by Channel (Revenue per ₹1 Spent)

### **🔍 Key Insights from the Chart:**

#### Online Marketing Performs Better:

- Across all months, online channels consistently yield higher revenue per rupee spent than offline.

- Peaks are visible in March, July, and November, suggesting these months had particularly successful digital campaigns.

- Offline Marketing Yields Lower Returns:

- The offline spend effectiveness remains relatively flat and consistently underperforms online spend.

- Lowest performance is observed in February and June, indicating poor campaign effectiveness during those periods.

---

### **_💡Strategic Recommendations:_**

#### Reallocate Budget Toward Online Channels:

- Given its consistently higher ROI, consider increasing online marketing spend by reducing allocation to offline campaigns.

#### Investigate Underperforming Months:

- Months like February and June had low offline and online effectiveness.

- Analyze campaign messaging, audience targeting, or external factors like seasonality.

#### Focus Online Spend on Peak Months:

- March, July, and November yielded top online effectiveness — replicate and expand those campaigns.

- Consider pre-launch buzz and retargeting to further enhance performance.

#### Refine Offline Marketing Tactics:

- If offline remains essential (e.g., branding), switch to performance-driven offline tactics like QR-based tracking or store-visit coupons.

#### Channel Attribution Modeling:

- Understand how channels interact in multi-touch journeys. Online may assist offline (or vice versa), so insights should drive cross-channel synergy.

#### Run Controlled Budget Experiments:

- A/B test budget splits (e.g., 70/30 vs. 50/50 online/offline) and measure which mix gives the highest return per campaign type.

### Q.10 Segment customers into groups such as Premium, Gold, Silver, and Standard. What targeted strategies can be developed for each segment to improve retention and revenue? (Use RFM segmentation techniques)

![q10.1](./images/q10.1.png)

![q10.2](./images/q10.2.png)

![q10.3](./images/q10.3.png)

### **Logic Used:**

- Calculate R,F,M metrics for each customer after grouping them from transaction data.
- Segment customers according to a set rule in to different tiers.

---

### 🧠 Strategic Insights & Actions

#### 🔶 Gold Segment

- Insight: High retention, balanced frequency and spending.

- Action:

  - Offer personalized incentives to move them to Premium.

  - Promote upgrade bundles or “VIP status” benefits.

  - Launch loyalty points for frequency boosts.

#### 🟡 Premium Segment

- Insight: Most recent customers, low frequency, but highly loyal.

* Action:

  - Drive repeat purchases with limited-time offers.

  - Introduce early-access or referral programs.

  - Target with upselling campaigns to increase their spend.

#### ⚪ Silver Segment

- Insight: Very frequent, high spend, but poor retention.

- Action:

  - Investigate pain points — post-purchase experience, delivery, or service.

  - Send satisfaction surveys and intervene with support.

  - Offer renewal discounts or loyalty-based tier upgrade plans.

#### ⚫ Standard Segment

- Insight: Oldest customer group, least recent, yet retention is highest — possibly repeat yearly or seasonal buyers.

- Action:

  - Trigger seasonal re-engagement campaigns.

  - Provide anniversary offers based on last purchase.

  - Use reactivation emails or SMS to stay top-of-mind.

---

#### ✅ Recommendation:

- Use this segmentation to:

  - Prioritize retention for Gold and Premium.

  - Re-engage Silver and Standard segments with personalized and

## Q.11 Analyze the revenue contribution of each customer segment. How can the company focus its efforts on high-value segments while nurturing lower-value segments?

![q11](./images/q11.png)

### **📊 Final Segment Summary:**

| Segment  | Revenue (₹)   | Revenue % | Frequency | Recency | Retained | Insight                                   |
| -------- | ------------- | --------- | --------- | ------- | -------- | ----------------------------------------- |
| Standard | ₹3,249,525.91 | 69.57%    | 622       | 364     | 332      | Large customer base, low individual value |
| Silver   | ₹1,129,541.81 | 24.18%    | 550       | 220     | 297      | Strong potential, good retention          |
| Gold     | ₹282,152.85   | 6.04%     | 264       | 131     | 100      | High engagement, small volume             |
| Premium  | ₹9,574.05     | 0.20%     | 32        | 49      | 5        | Very weak segment — likely misclassified  |

---

### **🔍 Insights by Segment:**

**🟥 Standard**

Contributes most revenue (69%).

Also has the highest number of retained customers (332).

But: recency = 364 days, i.e., they haven’t purchased in nearly a year.

Likely casual or one-time customers.

**🟦 Silver**

Great balance between retention, frequency, and recency.

Contributes a solid 24% of revenue.

This is your most nurture-ready segment.

**🟨 Gold**

High frequency and decent recency, but low revenue and small count.

This may be an under-promoted loyalist group.

**❌ Premium**

Only 0.2% of revenue with minimal retention or frequency.

---

### **🧠 Strategy Recommendations**

**✅ Standard (Broad Base, Low Depth)**

- Goal: Convert into repeat buyers.

Strategies:

- Post-purchase email automation

- Loyalty points for 2nd+ purchases

- Personalized product recommendations

**✅ Silver (High Potential)**

- Goal: Promote into Gold segment.

Strategies:

- Bundle offers or "Complete the Look"

- Referral bonuses

- Milestone-based rewards

**✅ Gold (Loyal, Low Volume)**

- Goal: Drive monetization through targeted upsell.

Strategies:

- Exclusive early access to new launches

- Limited-time higher-value bundles

- “Spend ₹X, earn Gold+ status” incentives

### **✅ Final Takeaway:**

- Your true value lies in nurturing Silver and converting Standard customers.
- Premium needs strict redefinition, and Gold deserves engagement-based monetization.

## Q12.Group customers by their month of first purchase and analyze retention rates over time. Which cohorts exhibit the highest and lowest retention rates? What strategies can be implemented to improve retention for weaker cohorts?

![q12](./images/q12.png)

![q12](./images/q10.2.png)

### **Logic Used:**

- Pretty similar to Q4.

* Aggregate based on month of first purchase and not on current month of purchase.

---

#### Insights:

- The retention heatmap reveals which cohorts (grouped by first purchase month) retained customers better.

- A 100% rate might indicate a small cohort where all customers returned at least once, often early in the lifecycle.

#### Strategies to Improve Retention for Weaker Cohorts:

- Targeted Campaigns: Identify weaker cohorts and run personalized re-engagement campaigns.

- Loyalty Programs: Introduce reward systems for frequent buyers.

- Onboarding Experience: Improve first-month experience to build habit-forming behavior.

- Email & SMS Reminders: Follow up with inactivity alerts and product suggestions.

- Incentivize Feedback: Ask why they didn’t return and offer incentives to revisit.

- Special Offers: Offer exclusive discounts to dormant cohorts.

- Subscription Models: Encourage recurring purchases with subscriptions.

- Product Recommendations: Use data to suggest similar or complementary items.

- Reactivation Bonuses: Send limited-time deals to bring back inactive users.

- Analyze Timing: Understand if specific seasons or times influence churn.

## Q.13 Analyze the lifetime value of customers acquired in different months. How can this insight inform acquisition and retention strategies?

![q13](./images/q13.png)

### **Logic Used:**

- Aggregate based on Acquired Month -> Month of first purchase.

---

## 📊 Insight from the Graph: Total Revenue from Customers vs Acquired Month

This bar chart visualizes the total revenue generated from customers grouped by their month of acquisition (i.e., when they made their first purchase).

### **🔍 Key Observations:**

- January dominates in revenue generation, contributing over ₹1 million. This cohort significantly outperforms all others.

- There's a steady decline from February to June, indicating that customers acquired later tend to contribute less revenue.

- August shows the lowest revenue, suggesting weak customer acquisition or poor retention during this month.

- October to December show slight recovery, but still well below the early months.

---

### **🧠 Business Insights:**

**Strong Start in Q1: Customers acquired early in the year (Jan–Mar) tend to have higher revenue contribution, possibly due to:**

- New Year campaigns

- Fresh marketing budgets

- Early loyalty building

**Q3 Weakness (Jul–Sep):**

- Acquisition during these months might be less effective.

- Customers might be less engaged or not retained well.

- Seasonal slowness or ineffective campaigns could be factors.

---

### **✅ Strategic Recommendations:**

**For Acquisition:**

- Replicate Q1 strategies: Study the marketing, offers, and product trends from January to March and reuse or adapt them in slower months.

- Boost Q3 efforts: Increase marketing spend, optimize landing pages, and consider special mid-year sales to lift July–September performance.

**For Retention:**

- Introduce long-term engagement strategies for customers acquired after April.

- Provide time-sensitive incentives (e.g., loyalty points expiry, gamified challenges) to stimulate repeated purchases.

**For LTV Growth:**

- Consider nurturing lower-value cohorts through upsell and cross-sell campaigns.

- Segment these cohorts and run targeted win-back email/SMS campaigns.

## Q.14 Do customers who use coupons have a different average transaction value compared to those who do not?

### **Logic Used:**

- Perform statistical test on two groups.

---

### **🧪 Statistical Conclusion:**

- The p-value > 0.05, meaning the difference in transaction values is not statistically significant.

- Customers who use coupons do not spend significantly less or more than those who do not, at the transaction level.

---

### **🧠 Business Implications:**

- Coupons may not erode revenue per transaction as feared—this can justify their continued use.

- Since coupon users spend nearly the same, focus can shift to using coupons as acquisition or retention tools, rather than only price-slashing tactics.

---

**You can:**

- Use personalized coupon targeting for high-LTV cohorts.

- Introduce minimum spend thresholds to encourage higher order values when using coupons.

- Optimize campaigns to attract volume rather than value.

## Q.15 Do purchase behaviors (e.g., order frequency, order value) vary significantly across different demographic groups or pricing factors (e.g., delivery charges)?

![q15](./images/q15.png)

![q15.1](./images/q15.1.png)

![q15.2](./images/q15.2.png)

### 📊 Combined Insights from Graphs and Statistical Tests on Purchase Behavior

### **🔍 1. Revenue vs Location + Transaction Count (Graph 1 + ANOVA)**

- F-statistic = 3.24, p-value = 0.0114 → Significant Difference

  | Location      | Avg Revenue | #Transactions     | Insight                       |
  | ------------- | ----------- | ----------------- | ----------------------------- |
  | Washington DC | ₹93.62      | Low (~2700)       | High spenders, premium market |
  | New Jersey    | ₹90.98      | Low (~4500)       | High-value, niche market      |
  | New York      | ₹83.86      | High (~11,000)    | Low-value, high-volume market |
  | Chicago       | ₹88.46      | Highest (~18,000) | Popular but moderately priced |
  | California    | ₹89.39      | Very High         | Balanced performance          |

#### **📌 Implications:**

- Region matters: Revenue per transaction varies significantly by location.

**Personalized regional strategies are justified:**

- Upsell bundles in NY.

* Exclusive premium campaigns in Washington DC.

---

### **🔍 2. Revenue vs Delivery Tier (Graph 2 + ANOVA)**

- F-statistic = 212.6, p-value = 4.86e-48 → Highly Significant Difference

  | Delivery | Tier    | Avg Revenue        | #Transactions Insight                       |
  | -------- | ------- | ------------------ | ------------------------------------------- |
  | Low      | 77.72   | Highest (~27,000)  | Budget-friendly, high churn                 |
  | Mid      | ₹101.82 | Moderate (~16,000) | Best balance of volume and value            |
  | High     | ₹95.09  | Lowest (~10,000)   | Possibly premium shipping with fewer orders |

#### **📌 Implications:**

- Delivery pricing strongly influences spending.

**Consider:**

- Tiered pricing models: Incentivize upsells at mid-tier.

- Minimum order value for free shipping in low-tier zones.

- Premium delivery perks for high-tier buyers.

---

### **🔍 3. Heatmap: Revenue Across Location × Delivery Tier (Graph 3)**

**Observation Insight:**

- New Jersey Mid-tier = Highest revenue (₹114.56) Optimize promotions for this segment.
- Washington DC Mid-tier is also strong Push exclusive, premium delivery benefits.
- New York Low-tier = Lowest revenue Price-sensitive group—use discounts & volume offers.

### **💼 Strategic Recommendations:**

**🔹 Geo-Demographic Targeting**

- Customize campaigns based on location and delivery tier combinations.

- Prioritize high-potential pockets like New Jersey-mid and Washington DC-mid.

**🔹 Pricing Personalization**

Delivery-sensitive behavior warrants:

- Free shipping thresholds

- Bundled offers for high-tier zones

- Subscription models for high-frequency low-tier users

**🔹 Product Placement & Messaging**

- In New York, promote "value-for-money" products.

- In Washington DC, highlight exclusivity, speed, and concierge-like services.

## Q.16 Does customer tenure impact purchase frequency?

![q16](./images/q16.png)

### **Logic Used:**

- Get tenures from customers data.
- Compute freq of each customer from transactions data.

---

### 📈 Analysis: Customer Tenure vs Purchase Frequency

- The scatter plot titled "Customer Tenure vs Purchase Frequency" provides a visual understanding of how long a customer has been associated with the company (in months) and how often they have purchased.

---

### **🔍 Observations from the Plot:**

**Highly Scattered Relationship:**

- The data points are widely spread with no clear upward or downward trend.

- Customers with both short and long tenure exhibit high and low frequencies.

**Few High-Frequency Outliers:**

- A handful of customers make over 300–700 purchases, but these are rare and not tenure-dependent.

**Clustered Low-Activity Majority:**

- Most customers, regardless of tenure, have fewer than 100 transactions.

- There is no strong clustering toward higher frequency with longer tenure.

**Flat Correlation:**

(As seen from the plot and confirmed by earlier result: correlation ≈ 0.011) → virtually no linear relationship between tenure and purchase frequency.

---

### **✅ Conclusion:**

- Customer tenure does not significantly impact purchase frequency.

- This means just because a customer has been around longer doesn’t guarantee they'll purchase more often.

---

### **💡 Strategic Implications:**

**🔹 1. Don't Rely Solely on Time-Based Loyalty**

- Tenure is not a strong predictor of engagement.

- Focus instead on behavioral triggers, product affinity, or seasonal activity.

**🔹 2. Build Frequency via Engagement Campaigns**

Encourage repeat purchases via:

- Email nudges

Time-limited discounts

- Reward-based frequency programs

**🔹 3. Segment by Activity, Not Just Tenure**

- Segment users by recency + frequency, not just how long they've been customers.

      For example:

      "New & High Frequency"

      "Long-Term Dormant"

      "Churn-Risk Recent Joiners"

**🔹 4. Design Milestone Incentives**

- Celebrate tenure only if tied to meaningful activity.

      Example: “6-Month Anniversary — Here’s 10% Off Your Next Order!”

## Q.17 Analyze the relationship between delivery charges and order behavior.

![q17](./images/q17.png)

### **🔍 Visual Insight from Chart:**

| Delivery Tier | Order Frequency | Avg. Quantity | Avg. Revenue |
| ------------- | --------------- | ------------- | ------------ |
| Low           | ~27,000 orders  | ~3 items      | ₹77.72       |
| Mid           | ~16,000 orders  | ~3.4 items    | ₹101.82      |
| High          | ~10,000 orders  | ~10.2 items   | ₹95.09       |

---

### **🧠 Interpretation of Customer Behavior:**

**✅ Low Tier (Most Popular)**

- Dominates in volume, but has:

  - Lowest average revenue

  - Lowest quantity per transaction

  - Indicates price sensitivity.

* Customers likely favor low delivery fees even if it means smaller, frequent purchases.

**✅ Mid Tier (Sweet Spot)**

- Generates highest average revenue per transaction.

- Balanced frequency and decent order size.

- Suggests customers accept slightly higher delivery charges if value is clear.

**✅ High Tier (Bulk Buyers)**

- Fewest transactions but largest quantity per order.

- Revenue per transaction is strong, but less than mid-tier despite high quantities.

- Likely businesses or bulk shoppers who are willing to pay delivery fees for volume convenience.

---

### **📈 ANOVA Support:**

- F-statistic = 212.60, p-value ≈ 4.86e-48 → Strong evidence of significant behavioral differences across delivery tiers

---

### **🎯 Strategic Recommendations:**

**🔹 1. Optimize Mid-Tier Delivery Strategy**

- This is the most lucrative tier.

- Keep pricing as-is, or test small incentives like:

  - “Free delivery on your 3rd order this month”

  - “Rs. 20 cashback with mid-tier delivery”

**🔹 2. Grow Low-Tier Revenue**

- Introduce order-value based rewards:

  - “Spend ₹500, get free delivery”

  - “Flat ₹20 off on combos”

**🔹 3. Justify High-Tier Pricing**

- Offer exclusive perks:

  - Express delivery

  - Premium packaging

  - Loyalty points multipliers

- These buyers are valuable; make the experience worth the price.

**🔹 4. Segment Campaigns by Delivery Behavior**

- Use machine learning to cluster customers by their preferred tier and optimize personalized offers.

---

### **💡 Opportunities:**

Objective Strategy

- Increase revenue in low tier Push bundles, free shipping thresholds
- Maintain mid-tier profit Focus on value communication
- Boost high-tier conversions Premium services or subscription models

---

### **✅ Final Takeaway:**

- Delivery charges directly influence how often and how much customers order.
- Tailoring delivery pricing and perks to tier-specific behavior can unlock new revenue and retention growth.

## Q18. Evaluate how taxes and delivery charges influence customer spending behavior. Are there opportunities to adjust pricing strategies to improve customer satisfaction and revenue?

![q18.1](./images/q18.1.png)

![q18.2](./images/q18.2.png)

### 📊 Analysis: Impact of Taxes and Delivery Charges on Customer Spending Behavior

### **🔍 1. Revenue vs Tax Tier**

| Tax Tier | Revenue (₹)   | Observation                     |
| -------- | ------------- | ------------------------------- |
| Low      | ~3.6 million  | 🔝 Dominates revenue generation |
| High     | ~1.05 million | 🔻 Significant drop             |

**✅ Interpretation:**

- Low-tax items lead to far greater spending.

- Customers clearly prefer products with lower tax rates, possibly due to:

- Perceived savings

- Better affordability

---

### **🔍 2. Heatmap: Tax Tier × Delivery Tier**

| Tax Tier | Revenue-Low | Revenue-Mid     | Revenue-High | Insight                                                          |
| -------- | ----------- | --------------- | ------------ | ---------------------------------------------------------------- |
| Low      | High        | Highest         | High         | Customers spend more across all delivery tiers when tax is low.  |
| High     | Low         | Slightly Better | Moderate     | Even with higher delivery tiers, high-tax products underperform. |

**✅ Interpretation:**

- Even when delivery charges are low, high-tax products still perform poorly.

- Mid delivery tier + low tax is the best performing combo.

- High delivery + high tax is the least attractive combo for customers.

---

### **🧠 Strategic Implications:**

🔹 1. Product Mix & Promotions

- Promote low-tax products aggressively—customers already prefer them.

- Bundle high-tax products with low-tax ones to balance perceived value.

🔹 2. Delivery Subsidy for High-Tax Products

- Reduce or eliminate delivery charges for high-tax product categories.

- “Free delivery on electronics” or “0 delivery fee on lifestyle items”

- Helps soften the price shock from high GST.

🔹 3. Dynamic Discounting

- For high-tax and high-delivery combos, apply seasonal or flash discounts.

- Incentivize bulk orders of high-tax products to dilute overall effective cost.

🔹 4. Segmented Campaigns

- Target high-value customers with discounts on high-tax categories.

- For budget customers, promote low-tax, mid-delivery tier bundles.

---

### **💡 Optimization Opportunities:**

- Target Behavior Strategy

- Reduce cart abandonment Reduce delivery on high-tax items

- Boost high-tax category sales Offer tax-absorbing discounts or cashback

- Encourage bundling Combine low-tax with high-tax items

- Maximize mid-tier margin Promote mid-delivery tier as “best value”

---

### **✅ Final Takeaway:**

- Taxes and delivery charges both heavily influence customer spending—
  especially together.
- Optimizing these two levers via tiered discounts, bundling, and dynamic delivery offers can significantly boost both customer satisfaction and revenue.

## Q.19 Identify seasonal trends in sales by category and location. How can the company prepare for peak and off-peak seasons to maximize revenue?

![q19](./images/q19.png)

### 📊 Seasonal Trend Analysis from Heatmaps:

### **🔍 A. Category-Wise Seasonal Trends**

| Product Category     | Peak Months        | Observations                                                                  |
| -------------------- | ------------------ | ----------------------------------------------------------------------------- |
| Nest-USA             | Jan, Mar, May, Dec | Most dominant category throughout the year; peaks in winter & gifting season. |
| Apparel              | Mar–May, Oct–Dec   | Seasonal fashion shifts and festive sales.                                    |
| Drinkware            | May–Aug            | Warm months driving hydration needs.                                          |
| Gift Cards           | Nov–Dec            | Holiday gifting trend.                                                        |
| Office Supplies      | Jan, Sept          | New Year restock and back-to-school spikes.                                   |
| Lifestyle, Bags      | Nov–Dec            | Likely tied to travel, holidays, and gifting.                                 |
| Notebooks & Journals | Jan                | New Year resolutions and productivity tools.                                  |

---

### **🔍 B. Location-Wise Seasonal Trends**

| Location      | High Months        | Insight                                                        |
| ------------- | ------------------ | -------------------------------------------------------------- |
| Chicago       | Oct–Dec, Jan, Mar  | Consistent strength; heavy end-of-year surge.                  |
| California    | Feb, May, Oct, Dec | Balanced across year; warm-weather state with summer interest. |
| New York      | Feb, May, Nov–Dec  | Peaks in gifting/festive months.                               |
| New Jersey    | Apr–Jun            | Subtle seasonal spring rise.                                   |
| Washington DC | Feb, Dec           | Spikes in winter, relatively low rest of the year.             |

---

### **📈 Overall Trends:**

- Q1 (Jan–Mar):

  - Strong for Nest-USA, Office, California, Chicago

  - Associated with renewal shopping: tech, productivity, restocks.

- Q2 (Apr–Jun):

  - Rising sales in Apparel, Drinkware, New Jersey, California

  - Spring fashion, summer essentials begin to pick up.

- Q3 (Jul–Sep):

  - Stable/Low across most categories.

  - Drinkware and some Apparel still active.

- Q4 (Oct–Dec):

  - 🔥 Peak sales period

  - Strong across nearly all high-revenue categories and cities.

  - Fueled by holiday gifting, cold-weather products, seasonal promotions.

---

## **🧠 Strategic Recommendations:**

📦 1. Inventory Management

- Stock high-demand SKUs for Q4 in Nest-USA, Apparel, Gift Cards, and Lifestyle.

- Maintain Drinkware, Apparel stock for Q2-Q3 in California and New Jersey.

🎯 2. Targeted Regional Campaigns
|Region | Strategy|
|-------|---------|
|Chicago | Boost Q4 advertising, loyalty points, and holiday bundles.|
|California | Push warm-weather items in Q2, year-round essentials.|
|New York | Leverage fashion and holiday gifting in Q2 and Q4.|
|Washington DC | Capitalize on end-of-year needs with tax-saving offers and gift campaigns.|

🛍️ 3. Seasonal Promotions

- Jan & Sept: Productivity (office), educational bundles.

- May–Aug: Summer essentials (drinkware, bags).

- Nov–Dec: Heavy holiday campaigns, including gift guides, combo deals, and flash sales.

📈 4. Data-Driven Campaign Calendar

- Create a seasonal marketing calendar tied to actual category-location data:

  E.g., “Apparel Flash Sale – April in New York”

  “Nest Smart Home Bundles – December in Chicago”

---

### **✅ Final Takeaway:**

- The heatmaps clearly show seasonal and regional patterns.
- Strategic timing of inventory, ads, and category pushes can significantly maximize revenue across quarters.

## Q.20 Analyze daily sales trends to identify high-performing and low-performing days. What strategies can be implemented to boost sales on slower days?

![q20](./images/q20.png)

### **📈 High-Performing Days:**

- Friday: ~1008 units/day

- Thursday: ~855 units/day

- Wednesday: ~765 units/day

* These mid-to-late week days are the most productive for sales volume.

---

### **📉 Low-Performing Days:**

- Tuesday: ~214 units/day

- Monday: ~230 units/day

- Early-week days are consistently underperforming in terms of order quantity.

---

### **🎯 Strategic Recommendations to Boost Sales on Slower Days:**

**🛍️ 1. Flash Sales or Daily Deals (Mon–Tues)**

- Run “Monday Kickstart Deals” or “Tuesday Temptations” to drive urgency.

- Offer time-limited discounts only valid on slower days.

**🎁 2. Personalized Email Campaigns**

- Target dormant users with incentives early in the week:

- Example: “Come back today and get 10% off – only this Tuesday!”

**🎯 3. Gamify Slow Days**

- Use loyalty points multipliers or spin-the-wheel promos to incentivize weekday purchases.

**🚚 4. Free Shipping or Delivery Coupons**

- Offer free shipping for orders placed on low-performing days.

**📢 5. Marketing Spend Adjustment**

- Shift a portion of online ad budget (e.g., Google Ads or Facebook retargeting) toward Mon–Tues.
