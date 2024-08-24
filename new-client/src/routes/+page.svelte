<script lang="ts">
	import {
		faJs,
		faReact,
		faPython,
		faVuejs,
		faSass,
		faPhp
	} from '@fortawesome/free-brands-svg-icons';
	import { FontAwesomeIcon } from '@fortawesome/svelte-fontawesome';

	import type { IconSet } from '../types';

	const ICONS: ReadonlyArray<IconSet> = [
		{
			icon: faJs,
			color: '#F0DB4F'
		},
		{
			icon: faReact,
			color: '#61DBFB'
		},
		{
			icon: faVuejs,
			color: '#42B883'
		},
		{
			icon: faPython,
			color: '#4B8BBE'
		},
		{
			icon: faPhp,
			color: '#B0B3D6'
		},
		{
			icon: faSass,
			color: '#CC6699'
		}
	];
</script>

<div class="home">
	<div>
		{#each ICONS as icon}
			<FontAwesomeIcon
				style={{
					paddingRight: 10
				}}
				icon={icon.icon}
				color={icon.color}
				pull="left"
				size="3x"
			/>
		{/each}
	</div>
	<div>RIGHT</div>
</div>

<style lang="scss">
	.home {
		display: flex;
	}
</style>
