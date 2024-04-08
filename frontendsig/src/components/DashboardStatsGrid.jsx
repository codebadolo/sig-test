import React from 'react'

export default function DashboardStatsGrid() {
	return (
		<div className="flex gap-4">
			<BoxWrapper>
			<div className="main"> 
			this  is  the  dashboard  grid pages </div>
			</BoxWrapper>
			
		</div>
	)
}

function BoxWrapper({ children }) {
	return <div className="bg-white rounded-sm p-4 flex-1 border border-gray-200 flex items-center">{children}</div>
}
