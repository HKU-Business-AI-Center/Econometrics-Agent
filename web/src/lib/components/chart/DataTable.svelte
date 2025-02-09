<script lang="ts">
	import {
		Table,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell
	} from 'flowbite-svelte';
	import DownloadFile from './DownloadFile.svelte';
	export let selectedItem: any;
	// 获取表头（从 selectedItem 第一个对象的键提取）
	// 监听 selectedItem 的变化，并更新 headers
	$: headers = selectedItem.content.length > 0 ? Object.keys(selectedItem.content[0]) : [];
</script>

<div class="w-full flex-1 flex flex-col bg-[#000000] overflow-auto gap-4 pl-4 pr-4">
	{#if selectedItem.content && Array.isArray(selectedItem.content) && selectedItem.content.length > 0}
		<div class="w-full flex-1 overflow-auto flex flex-col">
			<p class="text-xl text-gray-400 mb-2 font-semibold">Table: {selectedItem.file}</p>
			<Table items={selectedItem.content} placeholder="Search by maker name" hoverable={true}>
				<!-- 生成表头 -->
				<TableHead>
					{#each headers as header}
						<TableHeadCell style="min-width: 150px">{header}</TableHeadCell>
					{/each}
				</TableHead>

				<!-- 生成表格主体 -->
				<TableBody tableBodyClass="divide-y">
					{#each selectedItem.content as item}
						<TableBodyRow>
							{#each headers as header}
								<TableBodyCell>{item[header]}</TableBodyCell>
							{/each}
						</TableBodyRow>
					{/each}
				</TableBody>
			</Table>
		</div>
	{:else}
		<div class="text-center flex-1 w-full flex items-center justify-center">
			<div>
				<h2 class="text-xl font-semibold text-gray-800 mb-2">No File Found</h2>
				<p class="text-gray-500 mb-4">
					It seems like you haven't added any flie yet. Click below to add something.
				</p>
			</div>
		</div>
	{/if}
	<div class="w-full flex-0 h-[60px] flex justify-end items-center pl-4 pr-4">
		<DownloadFile fileRaw={selectedItem.content} fileName={selectedItem.file} />
	</div>
</div>
