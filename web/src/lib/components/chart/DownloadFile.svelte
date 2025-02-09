<script lang="ts">
	import { GradientButton, Tooltip } from 'flowbite-svelte';
	export let fileRaw: any;
	export let fileName: string;
	function jsonToCsv(jsonArray: any) {
		// 如果 jsonArray 为空，返回空字符串
		if (!jsonArray || jsonArray.length === 0) return '';

		// 获取所有的字段（对象的键），并拼接成 CSV 的头部
		const headers = Object.keys(jsonArray[0]);
		const csvRows = [];

		// 添加 CSV 表头
		csvRows.push(headers.join(','));

		// 遍历每一行数据
		for (const row of jsonArray) {
			// 逐行将对象的值转换为 CSV 格式的字符串
			const values = headers.map((header) => {
				const value = row[header] !== undefined ? row[header] : '';
				// 对每个值进行适当的处理，防止逗号或换行符影响格式
				return `"${String(value).replace(/"/g, '""')}"`;
			});
			csvRows.push(values.join(','));
		}

		// 将 CSV 行合并为一个单一的字符串，并返回
		return csvRows.join('\n');
	}
	function downloadFile() {
		const csvContent = jsonToCsv(fileRaw);
		console.log(csvContent);

		let blob = new Blob([csvContent], { type: 'text/csv' });
		let downloadTempLink = document.createElement('a');
		let fileHerf = window.URL.createObjectURL(blob);
		downloadTempLink.href = fileHerf;
		downloadTempLink.download = fileName;
		document.body.appendChild(downloadTempLink);
		downloadTempLink.click();
		document.body.removeChild(downloadTempLink);
		window.URL.revokeObjectURL(fileHerf);
	}
</script>

<div>
	<button
		id="hover"
		class="w-[100px] p-3 text-center text-white font-medium rounded-lg transition-all duration-300 ease-in-out transform bg-gradient-to-r from-blue-500 to-purple-600 shadow-lg hover:shadow-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50 disabled:opacity-50 disabled:cursor-not-allowed"
		on:click={downloadFile}
		disabled={!fileRaw || fileRaw.length === 0}>Download</button
	>
	{#if !fileRaw || fileRaw.length === 0}
		<Tooltip triggeredBy="#hover">No file selected</Tooltip>
	{/if}
</div>
