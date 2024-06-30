import random

class TreeNode:
    def __init__(self, tree_type, rarity):
        self.tree_type = tree_type
        self.rarity = rarity
        self.next = None

class TreeList:
    def __init__(self):
        self.head = None

    def add_tree(self, tree_type, rarity):
        new_tree = TreeNode(tree_type, rarity)
        if self.head is None:
            self.head = new_tree
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_tree

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

def main():
    import tkinter as tk
    from tkinter import messagebox

    tree_list = TreeList()
    trees_per_click = 1
    
    def get_tree_rarity():
        # Define rarity probabilities
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
        tree_count_label.config(text=f"Trees planted: {total_trees}")
        trees_per_click_label.config(text=f"Trees per click: {trees_per_click}")
        eco_score_label.config(text=f"Eco Score: {eco_score}")
    
    def show_trees():
        rarity_count = tree_list.get_rarity_count()
        message = "\n".join([f"{rarity}: {count}" for rarity, count in rarity_count.items()])
        messagebox.showinfo("Trees Planted", message)

    def buy_item(item):
        nonlocal trees_per_click
        if item == "Watering Can":
            trees_per_click += 1
        elif item == "Fertilizer":
            trees_per_click += 2
        update_tree_count()
        messagebox.showinfo("Purchase Successful", f"You bought a {item}!")

    # Setup the main application window
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

    show_trees_button = tk.Button(root, text="Show Planted Trees", command=show_trees)
    show_trees_button.pack(pady=10)

    store_label = tk.Label(root, text="Store:")
    store_label.pack(pady=10)

    buy_watering_can_button = tk.Button(root, text="Buy Watering Can (+1 tree per click)", command=lambda: buy_item("Watering Can"))
    buy_watering_can_button.pack(pady=5)

    buy_fertilizer_button = tk.Button(root, text="Buy Fertilizer (+2 trees per click)", command=lambda: buy_item("Fertilizer"))
    buy_fertilizer_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
