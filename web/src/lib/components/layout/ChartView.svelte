<script lang="ts">
	import { onMount } from 'svelte';
	import Tooltip from '../common/Tooltip.svelte';
	import DataTable from '../chart/DataTable.svelte';
	import FileList from '../chart/FileList.svelte';

	let fileList = `[
  {
    "file": "vehicles",
    "content": [
      {
        "id": 1, "maker": "Ford", "model": "F-150", "type": "Pickup",
        "year": 2023, "color": "Oxford White", "engine": "3.5L EcoBoost V6",
        "horsepower": 400, "mileage": 1500, "price": 48500,
        "isNew": true, "fuelType": "Gasoline", "transmission": "10-Speed Automatic",
        "seatingCapacity": 5, "warrantyYears": 5
      },
      {
        "id": 2, "maker": "Toyota", "model": "Camry", "type": "Sedan",
        "year": 2022, "color": "Black", "engine": "2.5L Inline-4",
        "horsepower": 203, "mileage": 5000, "price": 28500,
        "isNew": false, "fuelType": "Gasoline", "transmission": "8-Speed Automatic",
        "seatingCapacity": 5, "warrantyYears": 3
      },
            {
        "id": 3, "maker": "Toyota", "model": "Camry", "type": "Sedan",
        "year": 2022, "color": "Black", "engine": "2.5L Inline-4",
        "horsepower": 203, "mileage": 5000, "price": 28500,
        "isNew": false, "fuelType": "Gasoline", "transmission": "8-Speed Automatic",
        "seatingCapacity": 5, "warrantyYears": 3
      },
            {
        "id": 4, "maker": "Toyota", "model": "Camry", "type": "Sedan",
        "year": 2022, "color": "Black", "engine": "2.5L Inline-4",
        "horsepower": 203, "mileage": 5000, "price": 28500,
        "isNew": false, "fuelType": "Gasoline", "transmission": "8-Speed Automatic",
        "seatingCapacity": 5, "warrantyYears": 3
      },
            {
        "id": 5, "maker": "Toyota", "model": "Camry", "type": "Sedan",
        "year": 2022, "color": "Black", "engine": "2.5L Inline-4",
        "horsepower": 203, "mileage": 5000, "price": 28500,
        "isNew": false, "fuelType": "Gasoline", "transmission": "8-Speed Automatic",
        "seatingCapacity": 5, "warrantyYears": 3
      },
            {
        "id": 6, "maker": "Toyota", "model": "Camry", "type": "Sedan",
        "year": 2022, "color": "Black", "engine": "2.5L Inline-4",
        "horsepower": 203, "mileage": 5000, "price": 28500,
        "isNew": false, "fuelType": "Gasoline", "transmission": "8-Speed Automatic",
        "seatingCapacity": 5, "warrantyYears": 3
      },
			{
        "id": 29, "maker": "Tesla", "model": "Model S", "type": "Sedan",
        "year": 2024, "color": "Midnight Silver", "engine": "Electric",
        "horsepower": 670, "mileage": 500, "price": 89990,
        "isNew": true, "fuelType": "Electric", "transmission": "Single-Speed",
        "seatingCapacity": 5, "warrantyYears": 8
      },
			{
        "id": 30, "maker": "Tesla", "model": "Model S", "type": "Sedan",
        "year": 2024, "color": "Midnight Silver", "engine": "Electric",
        "horsepower": 670, "mileage": 500, "price": 89990,
        "isNew": true, "fuelType": "Electric", "transmission": "Single-Speed",
        "seatingCapacity": 5, "warrantyYears": 8
      },
			{
        "id": 31, "maker": "Tesla", "model": "Model S", "type": "Sedan",
        "year": 2024, "color": "Midnight Silver", "engine": "Electric",
        "horsepower": 670, "mileage": 500, "price": 89990,
        "isNew": true, "fuelType": "Electric", "transmission": "Single-Speed",
        "seatingCapacity": 5, "warrantyYears": 8
      },
			{
        "id": 32, "maker": "Tesla", "model": "Model S", "type": "Sedan",
        "year": 2024, "color": "Midnight Silver", "engine": "Electric",
        "horsepower": 670, "mileage": 500, "price": 89990,
        "isNew": true, "fuelType": "Electric", "transmission": "Single-Speed",
        "seatingCapacity": 5, "warrantyYears": 8
      },
			{
        "id": 33, "maker": "Tesla", "model": "Model S", "type": "Sedan",
        "year": 2024, "color": "Midnight Silver", "engine": "Electric",
        "horsepower": 670, "mileage": 500, "price": 89990,
        "isNew": true, "fuelType": "Electric", "transmission": "Single-Speed",
        "seatingCapacity": 5, "warrantyYears": 8
      },
			{
        "id": 34, "maker": "Tesla", "model": "Model S", "type": "Sedan",
        "year": 2024, "color": "Midnight Silver", "engine": "Electric",
        "horsepower": 670, "mileage": 500, "price": 89990,
        "isNew": true, "fuelType": "Electric", "transmission": "Single-Speed",
        "seatingCapacity": 5, "warrantyYears": 8
      },
			{
        "id": 35, "maker": "Tesla", "model": "Model S", "type": "Sedan",
        "year": 2024, "color": "Midnight Silver", "engine": "Electric",
        "horsepower": 670, "mileage": 500, "price": 89990,
        "isNew": true, "fuelType": "Electric", "transmission": "Single-Speed",
        "seatingCapacity": 5, "warrantyYears": 8
      },
			{
        "id": 36, "maker": "Tesla", "model": "Model S", "type": "Sedan",
        "year": 2024, "color": "Midnight Silver", "engine": "Electric",
        "horsepower": 670, "mileage": 500, "price": 89990,
        "isNew": true, "fuelType": "Electric", "transmission": "Single-Speed",
        "seatingCapacity": 5, "warrantyYears": 8
      },
			{
        "id": 37, "maker": "Tesla", "model": "Model S", "type": "Sedan",
        "year": 2024, "color": "Midnight Silver", "engine": "Electric",
        "horsepower": 670, "mileage": 500, "price": 89990,
        "isNew": true, "fuelType": "Electric", "transmission": "Single-Speed",
        "seatingCapacity": 5, "warrantyYears": 8
      },
      {
        "id": 38, "maker": "Tesla", "model": "Model S", "type": "Sedan",
        "year": 2024, "color": "Midnight Silver", "engine": "Electric",
        "horsepower": 670, "mileage": 500, "price": 89990,
        "isNew": true, "fuelType": "Electric", "transmission": "Single-Speed",
        "seatingCapacity": 5, "warrantyYears": 8
      }
    ]
  },
  {
    "file": "customers",
    "content": [
      {
        "id": 1, "firstName": "Emily", "lastName": "Johnson", 
        "age": 34, "email": "emily.j@example.com", "phone": "+1-555-0234",
        "address": "123 Oak St, Springfield", "membershipLevel": "Gold",
        "lastPurchase": "2024-03-15", "totalSpent": 2450.50,
        "preferredPayment": "Credit Card", "newsletterSubscribed": true,
        "favoriteCategory": "Electronics", "accountCreated": "2021-02-14"
      },
      {
        "id": 2, "firstName": "David", "lastName": "Smith", 
        "age": 28, "email": "david.s@example.com", "phone": "+1-555-6789",
        "address": "456 Elm St, Springfield", "membershipLevel": "Silver",
        "lastPurchase": "2024-02-28", "totalSpent": 1375.75,
        "preferredPayment": "Debit Card", "newsletterSubscribed": false,
        "favoriteCategory": "Books", "accountCreated": "2020-06-10"
      },
      {
        "id": 28, "firstName": "Michael", "lastName": "Chen", 
        "age": 42, "email": "michael.c@example.com", "phone": "+1-555-9876",
        "address": "789 Pine Rd, Metropolis", "membershipLevel": "Platinum",
        "lastPurchase": "2024-04-01", "totalSpent": 18900.00,
        "preferredPayment": "PayPal", "newsletterSubscribed": true,
        "favoriteCategory": "Home Appliances", "accountCreated": "2019-11-05"
      }
    ]
  },
  {
    "file": "products",
    "content": [
      {
        "id": 1, "category": "Electronics", "name": "UltraHD Smart TV",
        "brand": "Sony", "price": 1499.99, "stockQuantity": 45,
        "releaseDate": "2024-01-15", "weightKg": 18.5,
        "dimensions": "56x32x8", "isWireless": false, "energyRating": "A++",
        "warrantyMonths": 24, "colorOptions": ["Black", "Silver"],
        "averageRating": 4.8, "supplier": "TechGlobal Inc"
      },
      {
        "id": 2, "category": "Appliances", "name": "Smart Refrigerator",
        "brand": "Samsung", "price": 2199.99, "stockQuantity": 20,
        "releaseDate": "2023-09-10", "weightKg": 95.2,
        "dimensions": "32x70x36", "isWireless": true, "energyRating": "A++",
        "warrantyMonths": 36, "colorOptions": ["Stainless Steel", "Black"],
        "averageRating": 4.7, "supplier": "HomeTech Ltd"
      },
      {
        "id": 30, "category": "Kitchen", "name": "Professional Blender",
        "brand": "Vitamix", "price": 599.99, "stockQuantity": 22,
        "releaseDate": "2023-11-01", "weightKg": 6.7,
        "dimensions": "18x18x45", "isWireless": true, "energyRating": "A+",
        "warrantyMonths": 84, "colorOptions": ["Red", "Black", "Stainless"],
        "averageRating": 4.9, "supplier": "HomeChef Ltd"
      }
    ]
  }
]

	`;

	let selectedItem: any[] = [];

	let show = false;
	onMount(async () => {
		if (window.innerWidth > 1024) {
			show = true;
		}
	});
</script>

<div
	class="h-screen max-h-[100dvh] min-h-screen {show
		? 'lg:fixed w-[700px]'
		: 'translate-x-[700px] w-[0px]'}  bg-black text-gray-200 shadow-2xl text-sm transition z-40 fixed top-0 right-0
        "
>
	<div
		class="fixed right-0 top-[50dvh] z-40 -translate-y-1/2 transition-transform translate-x-[-695px] md:translate-x-[-700px] rotate-0"
	>
		<Tooltip placement="left" content={`${show ? 'Close' : 'Open'} sidebar`} touch={false}>
			<button
				id="sidebar-toggle-button-2"
				class=" group"
				on:click={() => {
					show = !show;
				}}
				><span class="" data-state="closed"
					><div
						class="flex h-[72px] w-8 items-center justify-center opacity-20 group-hover:opacity-100 transition"
					>
						<div class="flex h-6 w-6 flex-col items-center">
							<div
								class="h-3 w-1 rounded-full bg-[#0f0f0f] dark:bg-white rotate-0 translate-y-[0.15rem] {show
									? 'group-hover:rotate-[-15deg]'
									: 'group-hover:rotate-[15deg]'}"
							/>
							<div
								class="h-3 w-1 rounded-full bg-[#0f0f0f] dark:bg-white rotate-0 translate-y-[-0.15rem] {show
									? 'group-hover:rotate-[15deg]'
									: 'group-hover:rotate-[-15deg]'}"
							/>
						</div>
					</div>
				</span>
			</button>
		</Tooltip>
	</div>
	<div class="overflow-auto w-full h-full flex flex-col">
		<FileList bind:fileList bind:selectedItem />
		<DataTable bind:selectedItem />
	</div>
</div>
