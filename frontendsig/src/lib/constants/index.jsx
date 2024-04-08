import {
	HiOutlineCog,
	HiOutlineCube,
	HiOutlineQuestionMarkCircle,
	HiOutlineViewGrid
} from 'react-icons/hi'

export const DASHBOARD_SIDEBAR_LINKS = [
	{
		key: 'dashboard',
		label: 'recherche',
		path: '/',
		icon: <HiOutlineViewGrid />
	},
	{
		key: 'products',
		label: 'Products',
		path: '/comptabilites',
		icon: <HiOutlineCube />
	},

]

export const DASHBOARD_SIDEBAR_BOTTOM_LINKS = [
	{
		key: 'settings',
		label: 'Settings',
		path: '/settings',
		icon: <HiOutlineCog />
	},
	{
		key: 'support',
		label: 'Help & Support',
		path: '/support',
		icon: <HiOutlineQuestionMarkCircle />
	}
]
