import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"

const DISPLAY_FIELDS: Record<string, string> = {
  drug_name: "Drug Name",
  aliases: "Aliases",
  developer: "Developer",
  partner: "Partner",
  partner_type: "Partner Type",
  target: "Target",
  mechanism: "Mechanism",
  modality: "Modality",
  stage: "Stage",
  status: "Status",
  confidence_rating: "Confidence",
  thesis_cluster: "Thesis Cluster",
  company_type: "Company Type",
  publicly_traded: "Public",
  ticker: "Ticker",
  patient_population: "Population",
  route_of_administration: "Route",
  key_biomarkers: "Biomarkers",
  next_catalyst: "Next Catalyst",
  catalyst_date: "Catalyst Date",
}

const FrontmatterTable: QuartzComponent = ({ fileData, displayClass }: QuartzComponentProps) => {
  const fm = fileData.frontmatter
  if (!fm) return null

  const entries: [string, string][] = []
  for (const [key, label] of Object.entries(DISPLAY_FIELDS)) {
    const val = (fm as Record<string, unknown>)[key]
    if (val === undefined || val === null || val === "") continue
    const display = Array.isArray(val) ? val.join(", ") : String(val)
    entries.push([label, display])
  }

  if (entries.length === 0) return null

  return (
    <details class={classNames(displayClass, "frontmatter-table")} open>
      <summary>Metadata</summary>
      <table>
        <tbody>
          {entries.map(([label, value]) => (
            <tr>
              <td class="fm-key">{label}</td>
              <td class="fm-val">{value}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </details>
  )
}

FrontmatterTable.css = `
.frontmatter-table {
  margin: 0.5rem 0 1.5rem 0;
  border: 1px solid var(--lightgray);
  border-radius: 6px;
  padding: 0.5rem 1rem;
  font-size: 0.85rem;
}
.frontmatter-table summary {
  cursor: pointer;
  font-weight: 600;
  color: var(--secondary);
  margin-bottom: 0.5rem;
}
.frontmatter-table table {
  width: 100%;
  border-collapse: collapse;
}
.frontmatter-table tr {
  border-bottom: 1px solid var(--lightgray);
}
.frontmatter-table tr:last-child {
  border-bottom: none;
}
.frontmatter-table td {
  padding: 0.3rem 0.5rem;
  vertical-align: top;
}
.frontmatter-table .fm-key {
  font-weight: 600;
  white-space: nowrap;
  width: 1%;
  color: var(--darkgray);
}
.frontmatter-table .fm-val {
  color: var(--dark);
}
`

export default (() => FrontmatterTable) satisfies QuartzComponentConstructor
