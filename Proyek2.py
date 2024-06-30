import random
import tkinter as tk
from tkinter import messagebox

class TreeNode:
    def __init__(self, tree_type, rarity):
        self.tree_type = tree_type
        self.rarity = rarity
        self.next = None

class TreeList:
    def __init__(self):
        self.head = None
        self.coins = 0

    def add_tree(self, tree_type, rarity):
        new_tree = TreeNode(tree_type, rarity)
        if self.head is None:
            self.head = new_tree
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_tree
        self.add_coins_based_on_rarity(rarity)

    def add_coins_based_on_rarity(self, rarity):
        if rarity == "Common":
            self.coins += 1
        elif rarity == "Uncommon":
            self.coins += 2
        elif rarity == "Rare":
            self.coins += 3
        elif rarity == "Epic":
            self.coins += 4

    def get_rarity_count(self):
        rarity_count = {"Common": 0, "Uncommon": 0, "Rare": 0, "Epic": 0}
        current = self.head
        while current is not None:
            rarity_count[current.rarity] += 1
            current = current.next
        return rarity_count

    def calculate_eco_score(self):
        score = 0
        current = self.head
        while current is not None:
            if current.rarity == "Common":
                score += 1
            elif current.rarity == "Uncommon":
                score += 2
            elif current.rarity == "Rare":
                score += 5
            elif current.rarity == "Epic":
                score += 10
            current = current.next
        return score

    def count_total_trees(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def get_coins(self):
        return self.coins










def main():
    tree_list = TreeList()
    trees_per_click = 1
    watering_can_level = 0
    fertilizer_level = 0

    def get_tree_rarity():
        rarity_probabilities = {
            "Common": 0.6,
            "Uncommon": 0.25,
            "Rare": 0.1,
            "Epic": 0.05
        }
        rarity = random.choices(
            list(rarity_probabilities.keys()), 
            weights=list(rarity_probabilities.values()), 
            k=1
        )[0]
        return rarity

    def plant_tree():
        nonlocal trees_per_click
        for _ in range(trees_per_click):
            tree_type = "Tree"
            rarity = get_tree_rarity()
            tree_list.add_tree(tree_type, rarity)
        update_tree_count()

    def update_tree_count():
        total_trees = tree_list.count_total_trees()
        eco_score = tree_list.calculate_eco_score()
        coins = tree_list.get_coins()
        tree_count_label.config(text=f"Trees planted: {total_trees}")
        trees_per_click_label.config(text=f"Trees per click: {trees_per_click}")
        eco_score_label.config(text=f"Eco Score: {eco_score}")
        coins_label.config(text=f"Coins: {coins}")
        watering_can_price_label.config(text=f"Watering Can price: {get_watering_can_price(watering_can_level)}")
        fertilizer_price_label.config(text=f"Fertilizer price: {get_fertilizer_price(fertilizer_level)}")

    def show_trees():
        rarity_count = tree_list.get_rarity_count()
        message = "\n".join([f"{rarity}: {count}" for rarity, count in rarity_count.items()])
        messagebox.showinfo("Trees Planted", message)

    def get_watering_can_price(level):
        return 200 + (level * 50)

    def get_fertilizer_price(level):
        return 350 + (level * 85)

    def buy_item(item):
        nonlocal trees_per_click, watering_can_level, fertilizer_level
        if item == "Watering Can":
            price = get_watering_can_price(watering_can_level)
            if tree_list.get_coins() >= price:
                tree_list.coins -= price
                trees_per_click += 1
                watering_can_level += 1
                messagebox.showinfo("Purchase Successful", f"You bought a {item}!")
            else:
                messagebox.showinfo("Purchase Failed", f"Not enough coins to buy a {item}.")
        elif item == "Fertilizer":
            price = get_fertilizer_price(fertilizer_level)
            if tree_list.get_coins() >= price:
                tree_list.coins -= price
                trees_per_click += 2
                fertilizer_level += 1
                messagebox.showinfo("Purchase Successful", f"You bought a {item}!")
            else:
                messagebox.showinfo("Purchase Failed", f"Not enough coins to buy a {item}.")
        update_tree_count()

    root = tk.Tk()
    root.title("Environment Clicker Game")

    plant_button = tk.Button(root, text="Plant a Tree", command=plant_tree)
    plant_button.pack(pady=10)

    tree_count_label = tk.Label(root, text="Trees planted: 0")
    tree_count_label.pack(pady=10)

    trees_per_click_label = tk.Label(root, text="Trees per click: 1")
    trees_per_click_label.pack(pady=10)

    eco_score_label = tk.Label(root, text="Eco Score: 0")
    eco_score_label.pack(pady=10)

    coins_label = tk.Label(root, text="Coins: 0")
    coins_label.pack(pady=10)

    show_trees_button = tk.Button(root, text="Show Planted Trees", command=show_trees)
    show_trees_button.pack(pady=10)

    store_label = tk.Label(root, text="Store:")
    store_label.pack(pady=10)
    
    watering_can_price_label = tk.Label(root, text="Watering Can price: 200")
    watering_can_price_label.pack(pady=10)

    fertilizer_price_label = tk.Label(root, text="Fertilizer price: 350")
    fertilizer_price_label.pack(pady=10)
    
    buy_watering_can_button = tk.Button(root, text="Buy Watering Can (+1 tree per click)", command=lambda: buy_item("Watering Can"))
    buy_watering_can_button.pack(pady=5)

    buy_fertilizer_button = tk.Button(root, text="Buy Fertilizer (+2 trees per click)", command=lambda: buy_item("Fertilizer"))
    buy_fertilizer_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
