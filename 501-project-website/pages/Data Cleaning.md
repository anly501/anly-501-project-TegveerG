# Data Cleaning

[![](../images/data_cleaning.jpeg)](https://www.iteratorshq.com/blog/data-cleaning-in-5-easy-steps/)

[## REKT Database (Python)](https://github.com/anly501/anly-501-project-TegveerG/blob/main/codes/Data_Cleaning/REKT_Database_Cleaning.ipynb)
---

[**Raw Data (first 5 rows)**](https://github.com/anly501/anly-501-project-TegveerG/tree/main/data/Raw%20Data/Python_REKT_Database_API)

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>project_name</th>
      <th>description</th>
      <th>name_categories</th>
      <th>token_name</th>
      <th>proof_archive_link</th>
      <th>technical_issue</th>
      <th>token_address</th>
      <th>logo_link</th>
      <th>date</th>
      <th>proof_link</th>
      <th>website_link</th>
      <th>webarchive_link</th>
      <th>twitter_link</th>
      <th>telegram_link</th>
      <th>our_post_link</th>
      <th>funds_lost</th>
      <th>funds_returned</th>
      <th>active</th>
      <th>git_hub</th>
      <th>git_hub_contract_link</th>
      <th>discord</th>
      <th>bug_bounty_program_link</th>
      <th>bug_bounty_program_company</th>
      <th>audit_code_conf</th>
      <th>is_verified_source_code</th>
      <th>is_public_team</th>
      <th>scam_type</th>
      <th>network</th>
      <th>scamNetworks</th>
      <th>auditedBy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3058</td>
      <td>Terra Classic</td>
      <td>&lt;p&gt;&lt;strong&gt;Quick Summary&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;A complex mixture of events and market dynamics cost the implosion of the $40b Terra (Classic) Network.&amp;nbsp;&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;Details of the Exploit&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;The Terra Luna Network was focused on its two native coins $LUNC and $USTC. $USTC was the algorithmic Stablecoin that was supposed to hold the peg to 1$ and $LUNC functioned as the satellite asset that absorbed $USTC’s volatility. This was achieved through a mint and burn functionality as well as by arbitrage which the former function inherently enabled.&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;$USTC rose to prominence in rapid fashion even surpassing $DAI in market cap. The Luna Foundation Group decided to start a new Curve4pool with $FRAX, $USTC, $USDC and $USDT as assets, excluding $DAI in an attempt to starve the most used StableCoin pool used by institutions the Curve3pool on the Ethereum network.&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;The migration of $USTC from the Curve3pool is the event that started the bankrun. In early May, the Luna Foundation Guard withdrew 250 million $USTC from the Curve3pool in preparation for the Curve4pool. Simultaneously, a handful of whales withdrew sizeable amounts from the anchor protocol, a crypto savings bank. The biggest wallet withdrew 347 million $USTC in total and bridged funds to the Curve3pool in order to swap for other assets. This movement of funds created an imbalance between $USTC and other Stablecoins in the pool, resulting in devaluation of $USTC on exchanges.&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;As a result of the tokenomics of $USTC and $LUNC the firesale of $USTC resulted in uncontrollable minting of the $LUNC token and a rapid fall in valuation. Additionally, the Terra network went down due to overload in transaction as market participants were panicking and trying to answer margin calls within the Anchor protocol. Eventually massive liquidations of collateral in the Anchor protocol would be incurred by investors.&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;Block Data Reference&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;Whale Addresses:&lt;/p&gt;&lt;p&gt;https://etherscan.io/address/0x8d47f08ebc5554504742f547eb721a43d4947d0a&lt;/p&gt;&lt;p&gt;https://etherscan.io/address/0x4b5e60cb1cd6c5e67af5e6cf63229d1614bb781c&lt;/p&gt;&lt;p&gt;https://etherscan.io/address/0x1df8ea15bb725e110118f031e8e71b91abaa2a06&lt;/p&gt;&lt;p&gt;https://etherscan.io/address/0xeb5425e650b04e49e5e8b62fbf1c3f60df01f232&lt;/p&gt;&lt;p&gt;https://etherscan.io/address/0x41339d9825963515e5705df8d3b0ea98105ebb1c&lt;/p&gt;&lt;p&gt;https://etherscan.io/address/0x68963dc7c28a36fcacb0b39ac2d807b0329b9c69&lt;/p&gt;&lt;p&gt;https://etherscan.io/address/0x9f705ff1da72ed334f0e80f90aae5644f5cd7784&lt;/p&gt;</td>
      <td>Stablecoin</td>
      <td>LUNC, USTC</td>
      <td>https://twitter.com/OnChainWizard/status/1524123935570382851, https://rekt.news/ru/luna-rekt/, https://mobile.twitter.com/hasufl/status/1523817151471230976</td>
      <td>None</td>
      <td>0x7e43d25EaD96B1058f671F6690ea705BA2C7e5B9, 0xa47c8bf37f92abed4a126bda807a7b7498661acd</td>
      <td>safe/files/scamDatabase/logo/62b31ccc0d07e.jpeg</td>
      <td>2022-5-8</td>
      <td>https://www.nansen.ai/research/on-chain-forensics-demystifying-terrausd-de-peg?utm_source=twitter&amp;utm_medium=organic&amp;utm_campaign=Research_USTdepeg_27May22, https://www.cnet.com/personal-finance/crypto/luna-crypto-crash-how-ust-broke-and-whats-next-for-terra/, https://www.fool.com/the-ascent/cryptocurrency/articles/binance-ceo-says-luna-collapse-left-him-poor-again/#:~:text=Key%20points,and%20make%20a%20new%20plan., https://medium.com/coinmonks/whats-happening-with-the-terra-luna-seed-money-exit</td>
      <td>https://www.terra.money/</td>
      <td>None</td>
      <td>https://twitter.com/terra_money</td>
      <td>https://t.me/TerraNetworkLobby</td>
      <td>None</td>
      <td>40000000000</td>
      <td>None</td>
      <td>1</td>
      <td>https://github.com/terra-money/</td>
      <td>None</td>
      <td>https://twitter.com/terra_money</td>
      <td>None</td>
      <td>None</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>{'type': 'Bank Run'}</td>
      <td>{}</td>
      <td>[{'networks_id': 1003, 'scam_database_id': 3058, 'networks': {'id': 1003, 'name': 'Terra Classic', 'icon_link': 'safe/files/network/terra-classic.png'}}]</td>
      <td>[{'audit_link': 'safe/files/audit/pdf/CertiK_Audit_for_Terra_v18.pdf', 'date': '2020-09-03T00:00:00.000Z', 'partner': {'id': 8, 'name': 'Certik', 'logo_link': 'safe/files/partner/logo/609520cbb1bba.png'}}]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2762</td>
      <td>Africrypt</td>
      <td>&lt;p&gt;&lt;strong&gt;Quick Summary&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;Ameer and Raees Cajee, the exchange's founders, were reported missing in June 2021 after alleging that almost $3.6 billion invested in the protocol was stolen in a "hack".&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;Details of the Exploit&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;Africrypt claimed to connect banks, payment providers and digital asset providers for seamless global money transfers.&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;In April 2021, the Africrypt case gained traction. At the time, one of the protocol's founders contacted investors to notify them that the protocol had been compromised. The creator asked that investors refrain from contacting attorneys or law authorities since doing so would "slow the recovery process."&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;However, Africrypt staff lost access to the exchange's back-end systems seven days before the claimed attack, making this report suspect. After receiving notice of the "hack" and its odd request not to contact attorneys or law enforcement, several investors hired a law firm Hanekom Attorneys. The investigation discovered that most of the bitcoin invested with the exchange had been withdrawn and moved through tumblers and mixers to make it harder to track.&amp;nbsp;&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;The founders of Africrypt are still at large and have not been found as the time of this writing.&lt;/p&gt;</td>
      <td>CeFi</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>safe/files/scamDatabase/logo/61e049352a11a.png</td>
      <td>2021-6-23</td>
      <td>https://finance.yahoo.com/news/africrypt-bitcoin-disappearance-174636634.html, https://www.bloomberg.com/news/articles/2021-06-23/s-african-brothers-vanish-and-so-does-3-6-billion-in-bitcoin</td>
      <td>https://africrypt.io/</td>
      <td>https://web.archive.org/web/20200921145240/https://africrypt.io/</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>3600000000</td>
      <td>None</td>
      <td>1</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>{'type': 'Exit Scam'}</td>
      <td>{}</td>
      <td>[{'networks_id': 1666600003, 'scam_database_id': 2762, 'networks': {'id': 1666600003, 'name': 'CEX', 'icon_link': 'safe/files/network/cex.png'}}]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2878</td>
      <td>PlusToken</td>
      <td>&lt;p&gt;&lt;strong&gt;Quick Summary&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;The perpetrators of one of the largest digital currency frauds have been sentenced to up to 11 years in prison. In addition, the PlusToken operators were penalized up to $900,000 by a Chinese court for their participation in the $2.25 billion Ponzi scam.&lt;br&gt;&lt;strong&gt;&lt;br&gt;Details of the Exploit&lt;/strong&gt;&lt;br&gt;Chen Bo established PlusToken in early 2018, posing as a South Korean wallet and exchange. It enticed investors by promising speedy and guaranteed returns. In the two years afterwards, Bo has recruited numerous others and spread the fraud to other Southeast Asian nations such as China, Cambodia, Malaysia, Vanuatu, and Vietnam.&lt;br&gt;&lt;br&gt;PlusToken operators had devised a pyramid scheme that managed to lure over 2.6 million investors, authorities said. The scam was organized into at least 3,200 investor levels, with more referrals and bigger investments bumping an investor up the chain. The operators also lied to investors that they were making money through digital currency investing, according to investors.&lt;/p&gt;</td>
      <td>CeFi</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>safe/files/scamDatabase/logo/62432b9d39213.png</td>
      <td>2019-12-16</td>
      <td>https://cointelegraph.com/news/vanuatu-extradicts-six-chinese-citizens-allegedly-involved-in-crypto-scheme, https://www.nasdaq.com/articles/ringleaders-of-plustoken-scam-jailed-for-up-to-11-years-2020-12-01, https://coingeek.com/plustoken-scam-top-operators-jailed-for-up-to-11-years/</td>
      <td>https://thecryptonizer.team-plt.com/</td>
      <td>https://web.archive.org/web/20220125033211/https://www.coindesk.com/policy/2020/12/01/ringleaders-of-plustoken-scam-jailed-for-up-to-11-years/</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>2900000000</td>
      <td>None</td>
      <td>1</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>{'type': 'Exit Scam'}</td>
      <td>{}</td>
      <td>[{'networks_id': 1666600003, 'scam_database_id': 2878, 'networks': {'id': 1666600003, 'name': 'CEX', 'icon_link': 'safe/files/network/cex.png'}}]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2861</td>
      <td>Thodex</td>
      <td>&lt;p&gt;&lt;strong&gt;Quick Summary&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;Thodex a turkish crypto exchange went down with other $2 billion of user funds entangled in massive fraud and mismanagement.&lt;strong&gt;&lt;br&gt;&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;Details of the Exploit&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;According to a translated statement on the website, Thodex, a crypto exchange that is located in Turkey, stated its platform has been "temporarily stopped" to handle an "abnormal fluctuation in the company accounts."&lt;br&gt;&lt;br&gt;According to local media, Thodex's founder, Faruk Fatih Özer, has gone to Albania with $2 billion of investors' funds. The Demiroren News Agency published a photo of Ozer departing Istanbul Airport:&lt;br&gt;https://www.dha.com.tr/gundem/thodexin-kurucusu-faruk-fatih-ozerin-havalimanindan-ayrilirken-fotografi-1822744&lt;/p&gt;&lt;p&gt;The CEO has since declared that he has been close to committing suicide but decided against it. According to his own words, Faruk Fatih Özer, plans to repay all investors before handing himself in to authorities.&lt;/p&gt;</td>
      <td>CeFi</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>safe/files/scamDatabase/logo/6241c6cb5dadc.jpeg</td>
      <td>2021-4-22</td>
      <td>https://www.cnbc.com/2021/04/23/bitcoin-btc-ceo-of-turkish-cryptocurrency-exchange-thodex-missing.html, https://www.dw.com/en/turkish-cryptocurrency-platform-founder-vanishes-fraud-suspected/a-57302955</td>
      <td>https://www.thodex.com/</td>
      <td>https://web.archive.org/web/20220405133149/https://coingeek.com/missing-thodex-ceo-may-face-40000-years-behind-bars-in-new-indictment/</td>
      <td>https://twitter.com/thodexofficial</td>
      <td>None</td>
      <td>None</td>
      <td>2000000000</td>
      <td>None</td>
      <td>1</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>{'type': 'Exit Scam'}</td>
      <td>{}</td>
      <td>[{'networks_id': 1666600003, 'scam_database_id': 2861, 'networks': {'id': 1666600003, 'name': 'CEX', 'icon_link': 'safe/files/network/cex.png'}}]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2735</td>
      <td>BitConnect</td>
      <td>&lt;p&gt;&lt;strong&gt;Quick Summary&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;BitConnect was a Ponzi Scheme that managed to raise approx. $2 billion dollars from investors before it collapsed.&lt;/p&gt;&lt;p&gt;&lt;strong&gt;&lt;br&gt;Details of the Exploit&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;BitConnect is a crypto lending platform, which claimed it used a trading bot for earning interest.&lt;br&gt;&lt;br&gt;In fact, BitConnect was suspected of being a Ponzi scheme because of its multilevel marketing structure and impossibly high payouts (1% daily compounded interest). BitConnect interest fluctuated greatly with the volatility of Bitcoin, which its value was tied to.&lt;br&gt;&lt;br&gt;The BitConnect Coin was among the world's top 20 most successful cryptocurrency tokens until its price collapsed after traders began losing confidence. BCC rose from a post ICO price of $0.17 to an all-time high of US$463 in December 2017; it declined to US$0.40 as of March 11, 2019. BitConnect released outstanding loans at a rate of US$363.62 to the BitConnect Wallet in form of BCC. However, soon after that news the internal exchange price and liquidity collapsed resulting in a nearly complete loss of value. Prosecutors managed to seize crypto assets worth $57 million from Arcaro, BitConnect's biggest partner in North America.&lt;/p&gt;</td>
      <td>Borrowing and Lending,CeFi</td>
      <td>BCC</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>safe/files/scamDatabase/logo/61bb58e866760.jpeg</td>
      <td>2018-1-15</td>
      <td>None</td>
      <td>https://www.bitconnect.co/</td>
      <td>https://web.archive.org/web/20220426131429/https://economictimes.indiatimes.com/tech/technology/bitconnects-satish-kumbhani-charged-by-us-in-2-4-billion-ponzi-scam/articleshow/89844151.cms, https://web.archive.org/web/20220709021515/https://www.theverge.com/2021/11/18/22789507/crypto-scam-government-bitconnect-56-million-victim-reimbursement, https://web.archive.org/web/20220604204802/https://edition.cnn.com/2022/02/27/business/bitconnect-ponzi-scheme-satish-kumbhani/index.html</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>2000000000</td>
      <td>56000000</td>
      <td>1</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>{'type': 'Exit Scam'}</td>
      <td>{}</td>
      <td>[{'networks_id': 1666600003, 'scam_database_id': 2735, 'networks': {'id': 1666600003, 'name': 'CEX', 'icon_link': 'safe/files/network/cex.png'}}]</td>
      <td>[]</td>
    </tr>
  </tbody>
</table>


After loading the record data and getting a quick view of it, we can move to cleaning/pre-processing the data. I first started with stripping off the whitespaces off the column names. Then, I went on to dropping variables that would not assist in our analysis. Most of the variables that we shall drop from our 31 columns are links to external sites, such as web archive, discord, and github. Moreover, these variables contain more than 2900 NaN values out of a total observation count of 3055. However, the variable proof_link could be important if I decide to scrape text data from the linked article about a crypto attack. We shall also get rid of the technical_issue field because it only contains 4 non-NaN values and, more importantly, does not have any insightful use. Therefore, I find it sensible to entirely remove these fields, instead of getting rid of their existing NaN values, for EDA and modeling purposes.

Next, we proceed to variable identification and typecasting, an important step to recognize what types of data our variables fit in.
For variables identified as Integer type, the summary is as follows:

*    `id` variable is a unique, nominal code indicating the token/coin associated with the crypto attack. Converting it to category type would not be beneficial due to the large number of unique tokens present in the database. **This variable should be converted to object/string type**. 

*    `active` variable most probably represents whether the crypto project is currently active in the market. I perused the API documentation to try to find this response variable's significance, but could not. Moreover, it has only taken on one as a value for ALL observations. This would mean that all crypto projects present in the database are still active. We could keep this variable for now, but **converting it to category would be better as it most likely would take on two values, either 1 (active) or 0 (inactive).**  

For variables identified as Object type, the summary is as follows:

*    Variables like `date`, `funds_lost`, and `funds_returned` are of type object. This means that **Pandas was not able to recognize the datatype** of these four variables. Therefore, we shall convert these aforementioned object data type variables to their respective datatypes. `funds_lost` and `funds_returned` are converted to floats and `date` is converted to pandas datetime.

For variables identified as Float type, the summary is as follows:

*   The `is_verified_source_code` and `is_public_team` variables take on the values of either 0 or 1. Hence, we convert them to category type.

***Extracting important time-based features for better EDA experience:***

The features from extracted are `month_of_attack`, `day_of_week_of_attack`, and `day_of_year_of_attack` from the raw date variable. 

### Removing HTML Tags from Description variable

We also have to clean a vital text variable in our dataset that will be used in NLP tasks later. This is the `description` variable, which verbosely lays out the proof of the attack taking place and verified links to where the reader can obtain more information. In order to process this column, I made use of the Beautiful Soup library's `.get_text` function and passed it in a for loop that looped through the 'description' variable and appended processed outputs to the `REKT_df` data frame. 

HOWEVER, a crucial step was missing, which was that of getting rid of all the NaN's present in the `description` variable. This variable itself has 285 missing values, but when we add the  `funds_lost` variable in the mix, the total missing values is only 284. The `funds_lost`variable is a highly valuable attribute and, possibly, a target variable for modeling. We cannot get rid of even that single observation that has a `funds_lost` value but no description. Therefore, seen in the two screenshots below, we could not get rid of ALL NaN's present in the `funds_lost` variable and `description` variable.

![](../images/REKT_Database_Rows_Removed)
![](../images/87th_highest_funds_lost_observation_missing_description)

The 284 rows were the only ones discarded while cleaning the dataset. Yes, there are missing values present in other rows, but we have done well to eliminate most, if not all, unnecessary data for EDA!

After all these above steps were completed, we come up with a cleaned data like this:

[**Clean Data (first 5 rows)**](https://github.com/anly501/anly-501-project-TegveerG/blob/main/data/Clean%20Data/REKT_Database_Clean_Python.csv)

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>project_name</th>
      <th>description</th>
      <th>name_categories</th>
      <th>token_name</th>
      <th>token_address</th>
      <th>date</th>
      <th>proof_link</th>
      <th>webarchive_link</th>
      <th>funds_lost</th>
      <th>funds_returned</th>
      <th>active</th>
      <th>is_verified_source_code</th>
      <th>is_public_team</th>
      <th>scam_type</th>
      <th>network</th>
      <th>scamNetworks</th>
      <th>auditedBy</th>
      <th>month_of_attack</th>
      <th>day_of_week_of_attack</th>
      <th>day_of_year_of_attack</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3058</td>
      <td>Terra Classic</td>
      <td>&lt;p&gt;&lt;strong&gt;Quick Summary&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;A complex mixture of events and market dynamics cost the implosion of the $40b Terra (Classic) Network.&amp;nbsp;&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;Details of the Exploit&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;The Terra Luna Network was focused on its two native coins $LUNC and $USTC. $USTC was the algorithmic Stablecoin that was supposed to hold the peg to 1$ and $LUNC functioned as the satellite asset that absorbed $USTC’s volatility. This was achieved through a mint and burn functionality as well as by arbitrage which the former function inherently enabled.&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;$USTC rose to prominence in rapid fashion even surpassing $DAI in market cap. The Luna Foundation Group decided to start a new Curve4pool with $FRAX, $USTC, $USDC and $USDT as assets, excluding $DAI in an attempt to starve the most used StableCoin pool used by institutions the Curve3pool on the Ethereum network.&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;The migration of $USTC from the Curve3pool is the event that started the bankrun. In early May, the Luna Foundation Guard withdrew 250 million $USTC from the Curve3pool in preparation for the Curve4pool. Simultaneously, a handful of whales withdrew sizeable amounts from the anchor protocol, a crypto savings bank. The biggest wallet withdrew 347 million $USTC in total and bridged funds to the Curve3pool in order to swap for other assets. This movement of funds created an imbalance between $USTC and other Stablecoins in the pool, resulting in devaluation of $USTC on exchanges.&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;As a result of the tokenomics of $USTC and $LUNC the firesale of $USTC resulted in uncontrollable minting of the $LUNC token and a rapid fall in valuation. Additionally, the Terra network went down due to overload in transaction as market participants were panicking and trying to answer margin calls within the Anchor protocol. Eventually massive liquidations of collateral in the Anchor protocol would be incurred by investors.&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;Block Data Reference&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;Whale Addresses:&lt;/p&gt;&lt;p&gt;https://etherscan.io/address/0x8d47f08ebc5554504742f547eb721a43d4947d0a&lt;/p&gt;&lt;p&gt;https://etherscan.io/address/0x4b5e60cb1cd6c5e67af5e6cf63229d1614bb781c&lt;/p&gt;&lt;p&gt;https://etherscan.io/address/0x1df8ea15bb725e110118f031e8e71b91abaa2a06&lt;/p&gt;&lt;p&gt;https://etherscan.io/address/0xeb5425e650b04e49e5e8b62fbf1c3f60df01f232&lt;/p&gt;&lt;p&gt;https://etherscan.io/address/0x41339d9825963515e5705df8d3b0ea98105ebb1c&lt;/p&gt;&lt;p&gt;https://etherscan.io/address/0x68963dc7c28a36fcacb0b39ac2d807b0329b9c69&lt;/p&gt;&lt;p&gt;https://etherscan.io/address/0x9f705ff1da72ed334f0e80f90aae5644f5cd7784&lt;/p&gt;</td>
      <td>Stablecoin</td>
      <td>LUNC, USTC</td>
      <td>0x7e43d25EaD96B1058f671F6690ea705BA2C7e5B9, 0xa47c8bf37f92abed4a126bda807a7b7498661acd</td>
      <td>2022-05-08</td>
      <td>https://www.nansen.ai/research/on-chain-forensics-demystifying-terrausd-de-peg?utm_source=twitter&amp;utm_medium=organic&amp;utm_campaign=Research_USTdepeg_27May22, https://www.cnet.com/personal-finance/crypto/luna-crypto-crash-how-ust-broke-and-whats-next-for-terra/, https://www.fool.com/the-ascent/cryptocurrency/articles/binance-ceo-says-luna-collapse-left-him-poor-again/#:~:text=Key%20points,and%20make%20a%20new%20plan., https://medium.com/coinmonks/whats-happening-with-the-terra-luna-seed-money-exit</td>
      <td>None</td>
      <td>4.000000e+10</td>
      <td>NaN</td>
      <td>1</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>{'type': 'Bank Run'}</td>
      <td>{}</td>
      <td>[{'networks_id': 1003, 'scam_database_id': 3058, 'networks': {'id': 1003, 'name': 'Terra Classic', 'icon_link': 'safe/files/network/terra-classic.png'}}]</td>
      <td>[{'audit_link': 'safe/files/audit/pdf/CertiK_Audit_for_Terra_v18.pdf', 'date': '2020-09-03T00:00:00.000Z', 'partner': {'id': 8, 'name': 'Certik', 'logo_link': 'safe/files/partner/logo/609520cbb1bba.png'}}]</td>
      <td>5.0</td>
      <td>6.0</td>
      <td>128.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2762</td>
      <td>Africrypt</td>
      <td>&lt;p&gt;&lt;strong&gt;Quick Summary&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;Ameer and Raees Cajee, the exchange's founders, were reported missing in June 2021 after alleging that almost $3.6 billion invested in the protocol was stolen in a "hack".&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;Details of the Exploit&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;Africrypt claimed to connect banks, payment providers and digital asset providers for seamless global money transfers.&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;In April 2021, the Africrypt case gained traction. At the time, one of the protocol's founders contacted investors to notify them that the protocol had been compromised. The creator asked that investors refrain from contacting attorneys or law authorities since doing so would "slow the recovery process."&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;However, Africrypt staff lost access to the exchange's back-end systems seven days before the claimed attack, making this report suspect. After receiving notice of the "hack" and its odd request not to contact attorneys or law enforcement, several investors hired a law firm Hanekom Attorneys. The investigation discovered that most of the bitcoin invested with the exchange had been withdrawn and moved through tumblers and mixers to make it harder to track.&amp;nbsp;&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;The founders of Africrypt are still at large and have not been found as the time of this writing.&lt;/p&gt;</td>
      <td>CeFi</td>
      <td>None</td>
      <td>None</td>
      <td>2021-06-23</td>
      <td>https://finance.yahoo.com/news/africrypt-bitcoin-disappearance-174636634.html, https://www.bloomberg.com/news/articles/2021-06-23/s-african-brothers-vanish-and-so-does-3-6-billion-in-bitcoin</td>
      <td>https://web.archive.org/web/20200921145240/https://africrypt.io/</td>
      <td>3.600000e+09</td>
      <td>NaN</td>
      <td>1</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>{'type': 'Exit Scam'}</td>
      <td>{}</td>
      <td>[{'networks_id': 1666600003, 'scam_database_id': 2762, 'networks': {'id': 1666600003, 'name': 'CEX', 'icon_link': 'safe/files/network/cex.png'}}]</td>
      <td>[]</td>
      <td>6.0</td>
      <td>2.0</td>
      <td>174.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2878</td>
      <td>PlusToken</td>
      <td>&lt;p&gt;&lt;strong&gt;Quick Summary&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;The perpetrators of one of the largest digital currency frauds have been sentenced to up to 11 years in prison. In addition, the PlusToken operators were penalized up to $900,000 by a Chinese court for their participation in the $2.25 billion Ponzi scam.&lt;br&gt;&lt;strong&gt;&lt;br&gt;Details of the Exploit&lt;/strong&gt;&lt;br&gt;Chen Bo established PlusToken in early 2018, posing as a South Korean wallet and exchange. It enticed investors by promising speedy and guaranteed returns. In the two years afterwards, Bo has recruited numerous others and spread the fraud to other Southeast Asian nations such as China, Cambodia, Malaysia, Vanuatu, and Vietnam.&lt;br&gt;&lt;br&gt;PlusToken operators had devised a pyramid scheme that managed to lure over 2.6 million investors, authorities said. The scam was organized into at least 3,200 investor levels, with more referrals and bigger investments bumping an investor up the chain. The operators also lied to investors that they were making money through digital currency investing, according to investors.&lt;/p&gt;</td>
      <td>CeFi</td>
      <td>None</td>
      <td>None</td>
      <td>2019-12-16</td>
      <td>https://cointelegraph.com/news/vanuatu-extradicts-six-chinese-citizens-allegedly-involved-in-crypto-scheme, https://www.nasdaq.com/articles/ringleaders-of-plustoken-scam-jailed-for-up-to-11-years-2020-12-01, https://coingeek.com/plustoken-scam-top-operators-jailed-for-up-to-11-years/</td>
      <td>https://web.archive.org/web/20220125033211/https://www.coindesk.com/policy/2020/12/01/ringleaders-of-plustoken-scam-jailed-for-up-to-11-years/</td>
      <td>2.900000e+09</td>
      <td>NaN</td>
      <td>1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>{'type': 'Exit Scam'}</td>
      <td>{}</td>
      <td>[{'networks_id': 1666600003, 'scam_database_id': 2878, 'networks': {'id': 1666600003, 'name': 'CEX', 'icon_link': 'safe/files/network/cex.png'}}]</td>
      <td>[]</td>
      <td>12.0</td>
      <td>0.0</td>
      <td>350.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2861</td>
      <td>Thodex</td>
      <td>&lt;p&gt;&lt;strong&gt;Quick Summary&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;Thodex a turkish crypto exchange went down with other $2 billion of user funds entangled in massive fraud and mismanagement.&lt;strong&gt;&lt;br&gt;&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;Details of the Exploit&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;According to a translated statement on the website, Thodex, a crypto exchange that is located in Turkey, stated its platform has been "temporarily stopped" to handle an "abnormal fluctuation in the company accounts."&lt;br&gt;&lt;br&gt;According to local media, Thodex's founder, Faruk Fatih Özer, has gone to Albania with $2 billion of investors' funds. The Demiroren News Agency published a photo of Ozer departing Istanbul Airport:&lt;br&gt;https://www.dha.com.tr/gundem/thodexin-kurucusu-faruk-fatih-ozerin-havalimanindan-ayrilirken-fotografi-1822744&lt;/p&gt;&lt;p&gt;The CEO has since declared that he has been close to committing suicide but decided against it. According to his own words, Faruk Fatih Özer, plans to repay all investors before handing himself in to authorities.&lt;/p&gt;</td>
      <td>CeFi</td>
      <td>None</td>
      <td>None</td>
      <td>2021-04-22</td>
      <td>https://www.cnbc.com/2021/04/23/bitcoin-btc-ceo-of-turkish-cryptocurrency-exchange-thodex-missing.html, https://www.dw.com/en/turkish-cryptocurrency-platform-founder-vanishes-fraud-suspected/a-57302955</td>
      <td>https://web.archive.org/web/20220405133149/https://coingeek.com/missing-thodex-ceo-may-face-40000-years-behind-bars-in-new-indictment/</td>
      <td>2.000000e+09</td>
      <td>NaN</td>
      <td>1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>{'type': 'Exit Scam'}</td>
      <td>{}</td>
      <td>[{'networks_id': 1666600003, 'scam_database_id': 2861, 'networks': {'id': 1666600003, 'name': 'CEX', 'icon_link': 'safe/files/network/cex.png'}}]</td>
      <td>[]</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>112.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2735</td>
      <td>BitConnect</td>
      <td>&lt;p&gt;&lt;strong&gt;Quick Summary&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;BitConnect was a Ponzi Scheme that managed to raise approx. $2 billion dollars from investors before it collapsed.&lt;/p&gt;&lt;p&gt;&lt;strong&gt;&lt;br&gt;Details of the Exploit&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;BitConnect is a crypto lending platform, which claimed it used a trading bot for earning interest.&lt;br&gt;&lt;br&gt;In fact, BitConnect was suspected of being a Ponzi scheme because of its multilevel marketing structure and impossibly high payouts (1% daily compounded interest). BitConnect interest fluctuated greatly with the volatility of Bitcoin, which its value was tied to.&lt;br&gt;&lt;br&gt;The BitConnect Coin was among the world's top 20 most successful cryptocurrency tokens until its price collapsed after traders began losing confidence. BCC rose from a post ICO price of $0.17 to an all-time high of US$463 in December 2017; it declined to US$0.40 as of March 11, 2019. BitConnect released outstanding loans at a rate of US$363.62 to the BitConnect Wallet in form of BCC. However, soon after that news the internal exchange price and liquidity collapsed resulting in a nearly complete loss of value. Prosecutors managed to seize crypto assets worth $57 million from Arcaro, BitConnect's biggest partner in North America.&lt;/p&gt;</td>
      <td>Borrowing and Lending,CeFi</td>
      <td>BCC</td>
      <td>None</td>
      <td>2018-01-15</td>
      <td>None</td>
      <td>https://web.archive.org/web/20220426131429/https://economictimes.indiatimes.com/tech/technology/bitconnects-satish-kumbhani-charged-by-us-in-2-4-billion-ponzi-scam/articleshow/89844151.cms, https://web.archive.org/web/20220709021515/https://www.theverge.com/2021/11/18/22789507/crypto-scam-government-bitconnect-56-million-victim-reimbursement, https://web.archive.org/web/20220604204802/https://edition.cnn.com/2022/02/27/business/bitconnect-ponzi-scheme-satish-kumbhani/index.html</td>
      <td>2.000000e+09</td>
      <td>56000000.0</td>
      <td>1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>{'type': 'Exit Scam'}</td>
      <td>{}</td>
      <td>[{'networks_id': 1666600003, 'scam_database_id': 2735, 'networks': {'id': 1666600003, 'name': 'CEX', 'icon_link': 'safe/files/network/cex.png'}}]</td>
      <td>[]</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2871</td>
      <td>WoToken</td>
      <td>&lt;p&gt;&lt;strong style='box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; outline: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); transition: background 0.45s ease-in 0s, background-color 0.45s ease-in 0s, border 0.45s ease-in 0s; font-weight: 700; font-family: "Avenir Next", sans-serif; color: rgb(5, 15, 25); font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(250, 251, 252); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'&gt;Quick Summary&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;WoToken scam took in roughly $1 billion worth of crypto at current prices from over 715,000 victims.&lt;/p&gt;&lt;p style='box-sizing: inherit; margin: 8px 0px 0px; padding: 0px; border: 0px; outline: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); transition: background 0.45s ease-in 0s, background-color 0.45s ease-in 0s, border 0.45s ease-in 0s; line-height: 1.4285em; font-family: "Avenir Next", sans-serif; overflow-wrap: break-word; color: rgb(5, 15, 25); font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 500; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(250, 251, 252); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'&gt;&lt;strong style='box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; outline: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); transition: background 0.45s ease-in 0s, background-color 0.45s ease-in 0s, border 0.45s ease-in 0s; font-weight: 700; font-family: "Avenir Next", sans-serif !important;'&gt;&lt;br style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; outline: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); transition: background 0.45s ease-in 0s, background-color 0.45s ease-in 0s, border 0.45s ease-in 0s; font-family: &amp;quot;Avenir Next&amp;quot;, sans-serif !important;"&gt;Details of the Exploit&lt;/strong&gt;&lt;/p&gt;&lt;p style='box-sizing: inherit; margin: 8px 0px 0px; padding: 0px; border: 0px; outline: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); transition: background 0.45s ease-in 0s, background-color 0.45s ease-in 0s, border 0.45s ease-in 0s; line-height: 1.4285em; font-family: "Avenir Next", sans-serif; overflow-wrap: break-word; color: rgb(5, 15, 25); font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 500; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(250, 251, 252); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'&gt;&lt;span style='color: rgb(5, 15, 25); font-family: "Avenir Next", sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 500; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(250, 251, 252); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'&gt;WoToken purported to create profits for users by deploying algorithmic trading bots and paying affiliates referral commissions. The stated proprietary trading program, however, did not exist, as with other MLM frauds.&lt;/span&gt;&lt;/p&gt;&lt;p style='box-sizing: inherit; margin: 8px 0px 0px; padding: 0px; border: 0px; outline: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); transition: background 0.45s ease-in 0s, background-color 0.45s ease-in 0s, border 0.45s ease-in 0s; line-height: 1.4285em; font-family: "Avenir Next", sans-serif; overflow-wrap: break-word; color: rgb(5, 15, 25); font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 500; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(250, 251, 252); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'&gt;One of the scam's key operators is allegedly tied to PlusToken, a multibillion-dollar Ponzi scheme that is thought to have influenced the price trajectory of Bitcoin (BTC) many times during 2019.&lt;br&gt;&lt;br&gt;WoToken amassed 46,000 BTC, over 2 million Ethereum (ETH), 292,000 Litecoin (LTC), 56,000 Bitcoin Cash (BCH), and 684,00 Eos (EOS) – totaling approximately $1 billion at the time of the arrest.&lt;br&gt;&lt;br&gt;WoToken was operational from July 2018 until October 2019.&lt;/p&gt;</td>
      <td>CeFi</td>
      <td>None</td>
      <td>None</td>
      <td>2020-05-14</td>
      <td>https://cointelegraph.com/news/plustoken-scammer-implicated-in-chinas-second-ten-figure-crypto-ponzi, https://www.theblockcrypto.com/linked/82783/china-crypto-ponzi-prison-wotoken-billions, https://news.bitcoin.com/billion-crypto-ponzi-wotoken-prison-china/</td>
      <td>https://web.archive.org/web/20181029073006/http://wotoken.pro/</td>
      <td>1.000000e+09</td>
      <td>NaN</td>
      <td>1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>{'type': 'Exit Scam'}</td>
      <td>{}</td>
      <td>[{'networks_id': 1666600003, 'scam_database_id': 2871, 'networks': {'id': 1666600003, 'name': 'CEX', 'icon_link': 'safe/files/network/cex.png'}}]</td>
      <td>[]</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>135.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2879</td>
      <td>Ronin</td>
      <td>&lt;p&gt;&lt;strong&gt;Quick Summary&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;The Ronin bridge has been exploited for 173,600 Ethereum and 25.5M USDC.&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;Details of the Exploit &amp;nbsp;&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;The Ronin Network, an Ethereum-based sidechain hosts the prominent play-to-earn game Axie Infinity.&lt;/p&gt;&lt;p&gt;The project team discovered that on March 23rd that Sky Mavis’s Ronin validator nodes and Axie DAO validator nodes were compromised resulting in 173,600 Ethereum and 25.5M USDC drained from the Ronin bridge in two transactions:&lt;br&gt;https://etherscan.io/tx/0xc28fad5e8d5e0ce6a2eaf67b6687be5d58113e16be590824d6cfa1a94467d0b7&lt;br&gt;https://etherscan.io/tx/0xed2c72ef1a552ddaec6dd1f5cddf0b59a8f37f82bdda5257d9c7c37db7bb9b08&lt;br&gt;&lt;br&gt;The attacker used hacked private keys in order to forge fake withdrawals. The validator key scheme is set up to be decentralized so that it limits an attack vector, but the attacker found a backdoor through a gas-free RPC node, which they abused to get the signature for the Axie DAO validator. Binance managed to identify and recover $5,8 million in funds spread across 86 accounts that had been moved to their exchange. In the aftermath of the Ronin bridge hack a Binance led funding round raised $150 million in order to partially repay users and ensure that operations will be sustained&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;&lt;strong style='box-sizing: border-box; font-family: "Open Sans", sans-serif; color: rgb(65, 65, 65); font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;'&gt;Block Data Reference&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;The hacker's address on Ethereum:&lt;br&gt;https://etherscan.io/address/0x098b716b8aaf21512996dc57eb0615e2383e2f96&lt;/p&gt;</td>
      <td>Bridge</td>
      <td>RON</td>
      <td>0xe514d9deb7966c8be0ca922de8a064264ea6bcd4</td>
      <td>2022-03-29</td>
      <td>https://twitter.com/Ronin_Network/status/1508828719711879168, https://roninblockchain.substack.com/p/community-alert-ronin-validators?s=w</td>
      <td>None</td>
      <td>6.250000e+08</td>
      <td>155800000.0</td>
      <td>1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>{'type': 'Exploit'}</td>
      <td>{}</td>
      <td>[{'networks_id': 1666600009, 'scam_database_id': 2879, 'networks': {'id': 1666600009, 'name': 'Ronin', 'icon_link': 'safe/files/network/ronin.png'}}]</td>
      <td>[]</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>88.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2543</td>
      <td>Poly Network</td>
      <td>&lt;p&gt;&lt;strong&gt;Quick Summary&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;&lt;span style='color: rgb(65, 65, 65); font-family: "Open Sans", sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'&gt;Polynetwork was hacked for $602M. The attacker used Proxy smart contracts on 3 chains.&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;&lt;br&gt;Details of the Exploit&lt;/strong&gt;&lt;/p&gt;&lt;p data-v-51e0c2ec=""&gt;&lt;span style='color: rgb(65, 65, 65); font-family: "Open Sans", sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'&gt;Polynetwork is a DeFi platform. The project was hacked for 602,189,570 $USD in various assets. The attacker used unverified bytecoded Proxy smart contracts on 3 chains. After the hack, the attacker who is called "Mr. White Hat", connected to the PolyNetwork team, and returned all stolen funds.&amp;nbsp;&lt;/span&gt;&lt;/p&gt;&lt;p data-v-51e0c2ec=""&gt;Security experts said, it was likely the attacker realizedit would be difficult for them to launder the money and cash out, since all transactions are recorded on the blockchain.&lt;/p&gt;&lt;p data-v-51e0c2ec=""&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;Block Data Reference&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;&amp;nbsp;Malicious smart contracts:&lt;/p&gt;&lt;p&gt;1. https://bscscan.com/address/0x7cea671dabfba880af6723bddd6b9f4caa15c87b#code&amp;nbsp;&lt;/p&gt;&lt;p&gt;2. https://polygonscan.com/address/0xabd7f7b89c5fd5d0aef06165f8173b1b83d7d5c9#code&amp;nbsp;&lt;/p&gt;&lt;p&gt;3. https://etherscan.io/address/0x838bf9e95cb12dd76a54c9f9d2e3082eaf928270#code&lt;br&gt;&lt;br&gt;The owner of the Proxy contract on ETH (which was used in the attack) is another bytecoded contract (https://etherscan.io/address/0x5a51E2ebF8D136926b9cA7b59B60464E7C44d2Eb) with the EOA ownership.&lt;br&gt;&lt;br&gt;EOA was previously funded from OKEX exchange:&lt;br&gt;https://etherscan.io/tx/0xe864536abe5440b56c9d0e600472519ed2eb84801507e24f8a6661f2c371be02&lt;br&gt;&lt;br&gt;Attacker’s addresses:&lt;br&gt;&lt;br&gt;Polygon:&lt;br&gt;https://polygonscan.com/address/0x5dc3603c9d42ff184153a8a9094a73d461663214&lt;br&gt;&lt;br&gt;Binance Smart Chain:&lt;br&gt;https://bscscan.com/address/0x0d6e286a7cfd25e0c01fee9756765d8033b32c71&lt;br&gt;&lt;br&gt;Ethereum:&lt;br&gt;https://etherscan.io/address/0xc8a65fadf0e0ddaf421f28feab69bf6e2e589963&lt;br&gt;&lt;br&gt;The attacker started to approve USDC and BUSD tokens in order to deposit them into Ellipsis stablecoin pool:&lt;br&gt;https://bscscan.com/tx/0x5fe51028a73821777c2dcaa575d73add58cac79b9f68504b85c4281bf691fce8&lt;br&gt;https://bscscan.com/tx/0x4c6eaf4b0c5e080f3547160c39dca23fdd0533e1db849b1c096bf6df2cab1ba4&lt;br&gt;&lt;br&gt;Deposited into Ellipsis stablecoin pool ($32,107,136.29 BUSD and $87,602,010.73 USDC):&lt;br&gt;https://bscscan.com/tx/0x6768b4848b6713347195330a1a31326d3c060a9a828d5b5ec51bc6653bcc9b4e&lt;br&gt;&lt;br&gt;The attacker started to approve USDC and DAI tokens in order to deposit them into Curve stablecoin pool:&lt;br&gt;https://etherscan.io/tx/0x6c0b80ddb2d706a1e4bfcdb1815e6d5999443f863a7e96b37460bde75b99683d&lt;br&gt;https://etherscan.io/tx/0xa51979f54f6c9a2883712f5e694d9c23cf11394982cce4119b70c254624b52ea&lt;br&gt;&lt;br&gt;Deposited into Curve stablecoin pool ($671,156.42 DAI and $96,299,898.44 USDC):&lt;br&gt;https://etherscan.io/tx/0xbc54deb446c8daa623611c062e2e49f374ef3a04ddb2a8f4b788c9e54eb14485&lt;br&gt;&lt;br&gt;&lt;u&gt;remove_liquidity_one_coin&lt;/u&gt;() - $96,643,770.34 DAI was removed backed to the exploiter’s address:&lt;br&gt;https://etherscan.io/tx/0x2465d4cf19d3bf557ea5eec8d57b1ad75c8378e68ba242139e7e186bf463c1a1&lt;br&gt;&lt;br&gt;Stolen funds:&lt;br&gt;&lt;br&gt;ETH chain:&lt;br&gt;616,082.58 Fei USD ($614,628)&lt;br&gt;26,109.06 WETH ($82,374,869)&lt;br&gt;33,431,197.73 USDT ($33,239,073)&lt;br&gt;14.47 renBTC ($656,638)&lt;br&gt;259,737,345,149.51 SHIB ($1,999,977)&lt;br&gt;43,023.75 UNI ($1,247,688)&lt;br&gt;673,227.94 DAI &amp;nbsp;($673,201)&lt;br&gt;1,032.12 WBTC ($46,946,198)&lt;br&gt;96,389,444.22 USDC ($96,375,567)&lt;br&gt;&lt;br&gt;BSC chain:&lt;br&gt;32,107,854.11 BUSD ($32,105,564)&lt;br&gt;1,023.88 BTCB ($46,574,710)&lt;br&gt;26,629.15 ETH ($83,821,409)&lt;br&gt;87,603,373.77 USDC ($87,600,346)&lt;br&gt;&lt;br&gt;Polygon chain:&lt;br&gt;85,089,610.911 USDC ($85,057,567)&lt;/p&gt;</td>
      <td>Other</td>
      <td>None</td>
      <td>None</td>
      <td>2021-08-10</td>
      <td>None</td>
      <td>None</td>
      <td>6.021896e+08</td>
      <td>602189570.0</td>
      <td>1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>{'type': 'Exploit'}</td>
      <td>{}</td>
      <td>[{'networks_id': 1, 'scam_database_id': 2543, 'networks': {'id': 1, 'name': 'Ethereum', 'icon_link': 'safe/files/network/ethereum.png'}}]</td>
      <td>[]</td>
      <td>8.0</td>
      <td>1.0</td>
      <td>222.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2643</td>
      <td>Coincheck</td>
      <td>&lt;p&gt;&lt;strong&gt;Quick Summary&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;On Jan. 26, about 523 million NEM (XEM) tokens, valued over $530 million at the time, were illicitly transferred from its hot wallet address, resulting in an anomalous drop in the Japanese exchange's balance.&lt;/p&gt;&lt;p&gt;&lt;strong&gt;&lt;br&gt;Details of the Exploit&lt;/strong&gt;&lt;br&gt;The attack was made possible by the company's technological issues and staff scarcity, which resulted in inadequate security measures. The stolen NEM were held on an internet-connected hot wallet rather than an offline cold wallet.&lt;br&gt;&lt;br&gt;Coincheck utilized their own funds to compensate all 260,000 impacted clients:&lt;br&gt;https://www.ft.com/content/6a761a60-2694-11e8-b27e-cc62a39d57a0&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;</td>
      <td>CeFi</td>
      <td>None</td>
      <td>None</td>
      <td>2018-01-26</td>
      <td>https://www.reuters.com/article/us-japan-cryptocurrency-q-a/the-coincheck-hack-and-the-issue-with-crypto-assets-on-centralized-exchanges-idUSKBN1FI0K4, https://fortune.com/2018/01/31/coincheck-hack-how/, https://www.coindesk.com/markets/2018/01/26/coincheck-confirms-crypto-hack-loss-larger-than-mt-gox/</td>
      <td>None</td>
      <td>5.340000e+08</td>
      <td>534000000.0</td>
      <td>1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>{'type': 'Exploit'}</td>
      <td>{}</td>
      <td>[{'networks_id': 1666600003, 'scam_database_id': 2643, 'networks': {'id': 1666600003, 'name': 'CEX', 'icon_link': 'safe/files/network/cex.png'}}]</td>
      <td>[]</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>26.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2808</td>
      <td>Mt. Gox (3)</td>
      <td>&lt;p&gt;&lt;strong&gt;Quick Summary&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;One of the world's largest exchanges, Mt. Gox, declared bankruptcy in 2014 after being hacked, while losing most of its assets. At the time of bankruptcy, the exchange held 200k $BTC.&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;Details of the Exploit&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;Mt. Gox was a bitcoin exchange based in Shibuya, Tokyo, Japan. Launched in 2010, it processed more than 70% of all Bitcoin (BTC) transactions worldwide by the beginning of 2014.&lt;/p&gt;&lt;p&gt;At the beginning of 2014, Mt Gox, a bitcoin exchange based in Japan, was the largest bitcoin exchange in the world, handling over 70% of all bitcoin transactions worldwide. By the end of February of that year, it was bankrupt.&lt;br&gt;Anyone who was using Mt. Gox lost access to their assets, and it has been a cautionary tale for crypto investors. While the assets weren’t all lost, anything that was left has been frozen for years.&lt;br&gt;The victim of a massive hack, Mt. Gox lost about 740,000 bitcoins (6% of all bitcoin in existence at the time), valued at the equivalent of €473 million at the time and over $3 billion at October 2017 prices. An additional $27 million was missing from the company’s bank accounts.&lt;/p&gt;</td>
      <td>CeFi</td>
      <td>None</td>
      <td>None</td>
      <td>2014-02-24</td>
      <td>https://www.coindesk.com/markets/2014/02/25/mt-gox-allegedly-loses-350-million-in-bitcoin-744400-btc-rumoured-to-be-insolvent/, https://www.reuters.com/investigates/special-report/bitcoin-gox/</td>
      <td>None</td>
      <td>4.730000e+08</td>
      <td>NaN</td>
      <td>1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>{'type': 'Exploit'}</td>
      <td>{}</td>
      <td>[{'networks_id': 1666600003, 'scam_database_id': 2808, 'networks': {'id': 1666600003, 'name': 'CEX', 'icon_link': 'safe/files/network/cex.png'}}]</td>
      <td>[]</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>55.0</td>
    </tr>
  </tbody>
</table>

Clean data with missing values pertaining to the description variable. 

[## Twitter Text (Python)](https://github.com/anly501/anly-501-project-TegveerG/blob/main/codes/Data_Cleaning/Twitter_API_cleaning.ipynb)
---

1. Count Vectorizer for Analyzing Cosine Similarity 

2. Regex -> `.str.lower().apply(lambda x: re.sub(r"(?:\@|https?\://)\S+", "", x))` along with NLTK stopwords and tokenizations functions allows us to calculate Perplexity for n-gram models.

3. Using the processed text from when Perplexity was applied, the same text can be used for Sentiment Analysis using Vader. EDA page with more detailed content!

[## News Text (R)](https://github.com/anly501/anly-501-project-TegveerG/blob/main/codes/Data_Cleaning/NEWSAPI_cleaning.Rmd)
---

Record data cleaned by subsetting variables that were not useful to EDA or modeling. Only the `author` variable has missing values. Moreover, this variable does not provide much insight to our data analysis as the newspaper source is more important. We can drop this variable without losing useful information for my project.
We must also clean the `source` column using `gsub()` because it contains dictionary values, including 2 keys, in the form of strings. We only need the name of the publishing organization and, hence, string operations will help us parse the column correctly.


