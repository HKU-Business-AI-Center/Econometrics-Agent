<script lang="ts">
	import {
		Table,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell
	} from 'flowbite-svelte';
	export let selectedItem: any[] = [];

	// 获取表头（从 selectedItem 第一个对象的键提取）
	// 监听 selectedItem 的变化，并更新 headers
	$: headers = selectedItem.length > 0 ? Object.keys(selectedItem[0]) : [];
</script>

<div class="w-full flex-1 bg-[#000000] overflow-auto">
	<Table items={selectedItem} placeholder="Search by maker name" hoverable={true}>
		<!-- 生成表头 -->
		<TableHead>
			{#each headers as header}
				<TableHeadCell style="min-width: 150px">{header}</TableHeadCell>
			{/each}
		</TableHead>

		<!-- 生成表格主体 -->
		<TableBody tableBodyClass="divide-y">
			{#each selectedItem as item}
				<TableBodyRow>
					{#each headers as header}
						<TableBodyCell>{item[header]}</TableBodyCell>
					{/each}
				</TableBodyRow>
			{/each}
		</TableBody>
	</Table>
</div>
