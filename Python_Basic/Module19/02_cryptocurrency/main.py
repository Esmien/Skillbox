def show_keys_values(data: dict) -> None:
    print('Ключи:', list(data.keys()))
    print('Значения:', list(data.values()))
def main(): #я дико извиняюсь, что все решения будут тут, а не в отдельных функциях,
            # но я не смог придумать сценарий многократного использования функций,
            # соответствующих заданию
    data = {
        "address": "0x544444444444",
        "ETH": {
            "balance": 444,
            "total_in": 444,
            "total_out": 4
        },
        "count_txs": 2,
        "tokens": [
            {
                "fst_token_info": {
                    "address": "0x44444",
                    "name": "fdf",
                    "decimals": 0,
                    "symbol": "dsfdsf",
                    "total_supply": "3228562189",
                    "owner": "0x44444",
                    "last_updated": 1519022607901,
                    "issuances_count": 0,
                    "holders_count": 137528,
                    "price": False
                },
                "balance": 5000,
                "totalIn": 0,
                "total_out": 0
            },
            {
                "sec_token_info": {
                    "address": "0x44444",
                    "name": "ggg",
                    "decimals": "2",
                    "symbol": "fff",
                    "total_supply": "250000000000",
                    "owner": "0x44444",
                    "last_updated": 1520452201,
                    "issuances_count": 0,
                    "holders_count": 20707,
                    "price": False
                },
                "balance": 500,
                "totalIn": 0,
                "total_out": 0
            }
        ]
    }

    show_keys_values(data)
    data["ETH"]["total_diff"] = 100
    data["tokens"][0]["fst_token_info"]["name"] = "doge"
    for token in data["tokens"]:
        data["ETH"]["total_out"] += token.pop("total_out")
    data["tokens"][1]["sec_token_info"]["total_price"] = data["tokens"][1]["sec_token_info"].pop("price")
if __name__ == '__main__':
    main()