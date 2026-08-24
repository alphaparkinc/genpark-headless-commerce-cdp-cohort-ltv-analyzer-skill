from client import HeadlessCommerceCdpCohortLtvAnalyzerClient

def main():
    client = HeadlessCommerceCdpCohortLtvAnalyzerClient()
    res = client.compute_cohort_analytics('influencer_affiliate', '2026-05')
    print('Cohort: ' + res['cohort_month'] + ' [' + res['acquisition_channel'] + ']')
    print('CAC: $' + str(res['blended_cac_usd']) + ' | 90-Day LTV: $' + str(res['day_90_ltv_usd']) + ' (LTV/CAC: ' + str(res['ltv_to_cac_ratio']) + 'x)')
    print('Repeat Rate: ' + str(res['repeat_purchase_rate_pct']) + '% | 12-Mo GMV: $' + str(res['predicted_12_month_revenue_usd']))

if __name__ == '__main__':
    main()
