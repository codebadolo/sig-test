
export default function Dashboard() {
	return (
		<div className="bg-gray-100 p-4">
		<header className="text-2xl font-bold p-4 bg-white shadow-md">Gestion élève</header>
		<div className="flex gap-4 p-4">
		  <div className="flex-1 bg-white p-4 shadow-md">
			<div className="grid grid-cols-2 gap-4">
			  <input
				className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
				value="1626"
				placeholder="ID"
			  />
			  <input
				className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
				value="École Maternelle Centre social de Nasara"
				placeholder="École"
			  />
			  <input
				className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
				value="Amir"
				placeholder="Prénom"
			  />
			  <input
				className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
				value="PS"
				placeholder="Classe"
			  />
			  <input
				className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
				value="Balma"
				placeholder="Nom"
			  />
			  <input
				className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
				value="1"
				placeholder="Ordine_Tipo"
			  />
			  <button
				type="button"
				role="combobox"
				aria-controls="radix-:r18:"
				aria-expanded="false"
				aria-autocomplete="none"
				dir="ltr"
				data-state="closed"
				className="flex h-10 w-full items-center justify-between rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
				id="etat"
			  >
				<span ></span>
				<svg
				  xmlns="http://www.w3.org/2000/svg"
				  width="24"
				  height="24"
				  viewBox="0 0 24 24"
				  fill="none"
				  stroke="currentColor"
				  stroke-width="2"
				  stroke-linecap="round"
				  stroke-linejoin="round"
				  className="h-4 w-4 opacity-50"
				  aria-hidden="true"
				>
				  <path d="m6 9 6 6 6-6"></path>
				</svg>
			  </button>
			  <div className="flex items-center space-x-2">
				<label for="sex">Sex</label>
				<button
				  type="button"
				  role="combobox"
				  aria-controls="radix-:r1b:"
				  aria-expanded="false"
				  aria-autocomplete="none"
				  dir="ltr"
				  data-state="closed"
				  data-placeholder=""
				  className="flex h-10 w-full items-center justify-between rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
				>
				  <span >M</span>
				  <svg
					xmlns="http://www.w3.org/2000/svg"
					width="24"
					height="24"
					viewBox="0 0 24 24"
					fill="none"
					stroke="currentColor"
					stroke-width="2"
					stroke-linecap="round"
					stroke-linejoin="round"
					className="h-4 w-4 opacity-50"
					aria-hidden="true"
				  >
					<path d="m6 9 6 6 6-6"></path>
				  </svg>
				</button>
			  </div>
			  <input
				className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
				placeholder="Date naissance"
				value="26/10/2020"
			  />
			  <input
				className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
				value="78482173 (père)"
				placeholder="Nro_Tenues"
			  />
			  <button
				type="button"
				role="combobox"
				aria-controls="radix-:r1c:"
				aria-expanded="false"
				aria-autocomplete="none"
				dir="ltr"
				data-state="closed"
				data-placeholder=""
				className="flex h-10 w-full items-center justify-between rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
				id="cs_py"
			  >
				<span  >CS_PY</span>
				<svg
				  xmlns="http://www.w3.org/2000/svg"
				  width="24"
				  height="24"
				  viewBox="0 0 24 24"
				  fill="none"
				  stroke="currentColor"
				  stroke-width="2"
				  stroke-linecap="round"
				  stroke-linejoin="round"
				  className="h-4 w-4 opacity-50"
				  aria-hidden="true"
				>
				  <path d="m6 9 6 6 6-6"></path>
				</svg>
			  </button>
			  <input
				className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
				placeholder="Date enquête"
			  />
			  <input
				className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
				placeholder="A_inscr"
				value="2023"
			  />
			  <input
				className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
				placeholder="Hand"
			  />
			  <input
				className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
				placeholder="Parent"
				value="Balma Abdoulaye (père)"
			  />
			  <input
				className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
				placeholder="Tel parent"
				value="78482173 (père)"
			  />
			</div>
			<textarea
			  className="flex min-h-[80px] w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 mt-4 h-24"
			  placeholder="Note étudiant"
			></textarea>
		  </div>
		  <div className="flex-1">
			<div className="bg-white p-4 shadow-md mb-4">
			  <div className="flex justify-between items-center mb-4">
				<h2 className="text-lg font-semibold">Transactions</h2>
				<button className="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 hover:bg-primary/90 h-10 px-4 py-2 bg-green-500 text-white">
				  + Paiement
				</button>
			  </div>
			  <div className="relative w-full overflow-auto">
				<table className="w-full caption-bottom text-sm">
				  <thead className="[&amp;_tr]:border-b">
					<tr className="border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted">
					  <th className="h-12 px-4 text-left align-middle font-medium text-muted-foreground [&amp;:has([role=checkbox])]:pr-0">
						Date
					  </th>
					  <th className="h-12 px-4 text-left align-middle font-medium text-muted-foreground [&amp;:has([role=checkbox])]:pr-0">
						Raison
					  </th>
					  <th className="h-12 px-4 text-left align-middle font-medium text-muted-foreground [&amp;:has([role=checkbox])]:pr-0">
						Montant
					  </th>
					  <th className="h-12 px-4 text-left align-middle font-medium text-muted-foreground [&amp;:has([role=checkbox])]:pr-0">
						Note
					  </th>
					</tr>
				  </thead>
				  <tbody className="[&amp;_tr:last-child]:border-0">
					<tr className="border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted">
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">25/09/2023</td>
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">INS</td>
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">500</td>
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">
						<svg
						  xmlns="http://www.w3.org/2000/svg"
						  width="24"
						  height="24"
						  viewBox="0 0 24 24"
						  fill="none"
						  stroke="currentColor"
						  stroke-width="2"
						  stroke-linecap="round"
						  stroke-linejoin="round"
						  className="cursor-pointer"
						>
						  <path d="M4 13.5V4a2 2 0 0 1 2-2h8.5L20 7.5V20a2 2 0 0 1-2 2h-5.5"></path>
						  <polyline points="14 2 14 8 20 8"></polyline>
						  <path d="M10.42 12.61a2.1 2.1 0 1 1 2.97 2.97L7.95 21 4 22l.99-3.95 5.43-5.44Z"></path>
						</svg>
					  </td>
					</tr>
					<tr className="border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted">
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">25/09/2023</td>
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">SCO</td>
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">10 000</td>
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">
						<svg
						  xmlns="http://www.w3.org/2000/svg"
						  width="24"
						  height="24"
						  viewBox="0 0 24 24"
						  fill="none"
						  stroke="currentColor"
						  stroke-width="2"
						  stroke-linecap="round"
						  stroke-linejoin="round"
						  className="cursor-pointer"
						>
						  <path d="M4 13.5V4a2 2 0 0 1 2-2h8.5L20 7.5V20a2 2 0 0 1-2 2h-5.5"></path>
						  <polyline points="14 2 14 8 20 8"></polyline>
						  <path d="M10.42 12.61a2.1 2.1 0 1 1 2.97 2.97L7.95 21 4 22l.99-3.95 5.43-5.44Z"></path>
						</svg>
					  </td>
					</tr>
					<tr className="border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted">
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">25/09/2023</td>
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">TEN</td>
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">4 000</td>
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">
						<svg
						  xmlns="http://www.w3.org/2000/svg"
						  width="24"
						  height="24"
						  viewBox="0 0 24 24"
						  fill="none"
						  stroke="currentColor"
						  stroke-width="2"
						  stroke-linecap="round"
						  stroke-linejoin="round"
						  className="cursor-pointer"
						>
						  <path d="M4 13.5V4a2 2 0 0 1 2-2h8.5L20 7.5V20a2 2 0 0 1-2 2h-5.5"></path>
						  <polyline points="14 2 14 8 20 8"></polyline>
						  <path d="M10.42 12.61a2.1 2.1 0 1 1 2.97 2.97L7.95 21 4 22l.99-3.95 5.43-5.44Z"></path>
						</svg>
					  </td>
					</tr>
					<tr className="border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted">
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">25/09/2023</td>
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">CAN</td>
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">4 000</td>
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">
						<svg
						  xmlns="http://www.w3.org/2000/svg"
						  width="24"
						  height="24"
						  viewBox="0 0 24 24"
						  fill="none"
						  stroke="currentColor"
						  stroke-width="2"
						  stroke-linecap="round"
						  stroke-linejoin="round"
						  className="cursor-pointer"
						>
						  <path d="M4 13.5V4a2 2 0 0 1 2-2h8.5L20 7.5V20a2 2 0 0 1-2 2h-5.5"></path>
						  <polyline points="14 2 14 8 20 8"></polyline>
						  <path d="M10.42 12.61a2.1 2.1 0 1 1 2.97 2.97L7.95 21 4 22l.99-3.95 5.43-5.44Z"></path>
						</svg>
					  </td>
					</tr>
					<tr className="border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted">
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">05/12/2023</td>
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">SCO</td>
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">7 500</td>
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">
						<svg
						  xmlns="http://www.w3.org/2000/svg"
						  width="24"
						  height="24"
						  viewBox="0 0 24 24"
						  fill="none"
						  stroke="currentColor"
						  stroke-width="2"
						  stroke-linecap="round"
						  stroke-linejoin="round"
						  className="cursor-pointer"
						>
						  <path d="M4 13.5V4a2 2 0 0 1 2-2h8.5L20 7.5V20a2 2 0 0 1-2 2h-5.5"></path>
						  <polyline points="14 2 14 8 20 8"></polyline>
						  <path d="M10.42 12.61a2.1 2.1 0 1 1 2.97 2.97L7.95 21 4 22l.99-3.95 5.43-5.44Z"></path>
						</svg>
					  </td>
					</tr>
					<tr className="border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted">
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">01/02/2024</td>
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">SCO</td>
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">7 500</td>
					  <td className="p-4 align-middle [&amp;:has([role=checkbox])]:pr-0">
						<svg
						  xmlns="http://www.w3.org/2000/svg"
						  width="24"
						  height="24"
						  viewBox="0 0 24 24"
						  fill="none"
						  stroke="currentColor"
						  stroke-width="2"
						  stroke-linecap="round"
						  stroke-linejoin="round"
						  className="cursor-pointer"
						>
						  <path d="M4 13.5V4a2 2 0 0 1 2-2h8.5L20 7.5V20a2 2 0 0 1-2 2h-5.5"></path>
						  <polyline points="14 2 14 8 20 8"></polyline>
						  <path d="M10.42 12.61a2.1 2.1 0 1 1 2.97 2.97L7.95 21 4 22l.99-3.95 5.43-5.44Z"></path>
						</svg>
					  </td>
					</tr>
				  </tbody>
				</table>
			  </div>
			  <div className="text-right mt-4 font-bold">Paiements totaux: 33 500</div>
			</div>
			<div className="bg-white p-4 shadow-md">
			  <h2 className="text-lg font-semibold mb-4">Rangs</h2>
			  <div className="grid grid-cols-2 gap-4">
				<div className="inline-flex w-fit items-center whitespace-nowrap rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 border-transparent bg-secondary text-secondary-foreground hover:bg-secondary/80">
				  Rang1
				</div>
				<div className="inline-flex w-fit items-center whitespace-nowrap rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 border-transparent bg-secondary text-secondary-foreground hover:bg-secondary/80">
				  Rang2
				</div>
				<div className="inline-flex w-fit items-center whitespace-nowrap rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 border-transparent bg-secondary text-secondary-foreground hover:bg-secondary/80">
				  Rang3
				</div>
				<div className="inline-flex w-fit items-center whitespace-nowrap rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 border-transparent bg-secondary text-secondary-foreground hover:bg-secondary/80">
				  RangAnno
				</div>
			  </div>
			</div>
		  </div>
		</div>
	  </div>
     
	)
}
