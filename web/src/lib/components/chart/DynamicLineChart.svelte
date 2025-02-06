<script lang="ts">
	import {
		TooltipComponent,
		TooltipComponentOption,
		LegendComponent,
		LegendComponentOption
	} from 'echarts/components';
	import { PieChart, PieSeriesOption } from 'echarts/charts';
	import { LabelLayout } from 'echarts/features';
	import { CanvasRenderer } from 'echarts/renderers';
	import { init, use } from 'echarts/core';
	import { Chart } from 'svelte-echarts';

	use([TooltipComponent, LegendComponent, PieChart, CanvasRenderer, LabelLayout]);

	type EChartsOption = echarts.ComposeOption<
		TooltipComponentOption | LegendComponentOption | PieSeriesOption
	>;
	var options: EChartsOption;
	options = {
		tooltip: {
			trigger: 'item'
		},
		legend: {
			top: '5%',
			left: 'center'
		},
		series: [
			{
				name: 'Access From',
				type: 'pie',
				radius: ['40%', '70%'],
				avoidLabelOverlap: false,
				padAngle: 5,
				itemStyle: {
					borderRadius: 10
				},
				label: {
					show: false,
					position: 'center'
				},
				emphasis: {
					label: {
						show: true,
						fontSize: 40,
						fontWeight: 'bold'
					}
				},
				labelLine: {
					show: false
				},
				data: [
					{ value: 1048, name: 'Search Engine' },
					{ value: 735, name: 'Direct' },
					{ value: 580, name: 'Email' },
					{ value: 484, name: 'Union Ads' },
					{ value: 300, name: 'Video Ads' }
				]
			}
		]
	};
</script>

<div class="w-full h-[400px]">
	<Chart {init} {options} theme="dark" />
</div>
