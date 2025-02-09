<script lang="ts">
	import { FileChartBarOutline } from 'flowbite-svelte-icons';
	export let fileList = '';
	export let selectedItem: any = {
		file: '',
		content: []
	};

	// 解析 JSON 字符串
	let files = [];
	try {
		files = JSON.parse(fileList);
	} catch (error) {
		console.error('Invalid JSON format:', error);
	}

	// 处理按钮点击事件
	function handleClick(item: any) {
		selectedItem = item;
		console.log(selectedItem);
	}
</script>

<div class="w-full h-[200px] bg-[#000000] overflow-auto p-4 flex flex-col gap-2 justify-center">
	{#each files as item (item.file)}
		<button
			class="w-[97%] p-3 text-left text-white font-medium rounded-lg transition-all duration-300 ease-in-out transform hover:w-full active:w-[95%] bg-gradient-to-r from-blue-500 to-purple-600 shadow-lg hover:shadow-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
			on:click={() => handleClick(item)}
		>
			<span>
				<FileChartBarOutline
					slot="icon"
					class="w-6 h-6 text-primary-500 bg-primary-100 dark:bg-primary-800 dark:text-primary-200"
				/>
				{item.file}
			</span>
		</button>
	{/each}
</div>
