"""
Given the weights and profits of N items, in the form of {profit, weight} 
put these items in a knapsack of capacity W to get the maximum total profit
in the knapsack. In Fractional Knapsack, we can break items for maximizing 
the total value of the knapsack.
Input: arr[] = {{60, 10}, {100, 20}, {120, 30}}, W = 50
Output: 240 
Explanation: By taking items of weight 10 and 20 kg and 2/3 fraction of 30 kg. 
Hence total price will be 60+100+(2/3)(120) = 240
"""
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
        
def fractional_knapsack(item_arr, capacity):
    item_arr.sort(key=lambda x: (x.profit/x.weight), reverse=True)
    final_profit=0 
    
    for item in item_arr:
        if item.weight <= capacity:
            final_profit += item.profit
            capacity -= item.weight
            
        else:
             final_profit += item.profit * capacity/item.weight 
             break
    return final_profit
    
if __name__ == "__main__":
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    capacity = 50
    
    maxm_profit = fractional_knapsack(arr, capacity)
    
    print("Maximizing Profit = ", maxm_profit)
    
    
