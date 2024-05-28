# Define a class for the Asset
class Asset:
    def __init__(self, asset_id, name, category, purchase_date, value):
        self.asset_id = asset_id
        self.name = name
        self.category = category
        self.purchase_date = purchase_date
        self.value = value

    def display_asset(self):
        print(f"Asset ID: {self.asset_id}")
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Purchase Date: {self.purchase_date}")
        print(f"Value: {self.value}")
        print()

# Define a class for Asset Management
class AssetManagement:
    def __init__(self):
        self.assets = []

    def add_asset(self, asset):
        self.assets.append(asset)
        print(f"Asset '{asset.name}' added successfully.\n")

    def display_all_assets(self):
        if not self.assets:
            print("No assets to display.")
        else:
            for asset in self.assets:
                asset.display_asset()

    def find_asset_by_id(self, asset_id):
        for asset in self.assets:
            if asset.asset_id == asset_id:
                return asset
        return None

# Function to create an asset
def create_asset():
    asset_id = input("Enter Asset ID: ")
    name = input("Enter Asset Name: ")
    category = input("Enter Asset Category: ")
    purchase_date = input("Enter Purchase Date (YYYY-MM-DD): ")
    value = input("Enter Asset Value: ")
    return Asset(asset_id, name, category, purchase_date, value)

# Main program execution
if __name__ == "__main__":
    asset_management = AssetManagement()

    while True:
        print("\nAsset Management System")
        print("1. Add Asset")
        print("2. Display All Assets")
        print("3. Find Asset by ID")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            asset = create_asset()
            asset_management.add_asset(asset)
        elif choice == '2':
            asset_management.display_all_assets()
        elif choice == '3':
            asset_id = input("Enter Asset ID to search: ")
            asset = asset_management.find_asset_by_id(asset_id)
            if asset:
                asset.display_asset()
            else:
                print("Asset not found.")
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

a1=Asset(1234,'amazon','original','12-02-2024')
a1.display_asset()