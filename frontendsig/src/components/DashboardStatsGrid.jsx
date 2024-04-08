import React from 'react'
import { HandStudent } from "./pages/HandStudent"
export default function DashboardStatsGrid() {
	return (
		<div className="flex gap-4">
			<BoxWrapper>
		
			<HandStudent></HandStudent>

			</BoxWrapper>
			
		</div>
	)
}

function BoxWrapper({ children }) {
	return <div className="bg-white rounded-sm p-4 flex-1 border border-gray-200 flex items-center">{children}</div>
}
