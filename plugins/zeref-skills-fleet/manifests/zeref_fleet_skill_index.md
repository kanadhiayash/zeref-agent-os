# Zeref Fleet Skills Index

Generated: 2026-05-07

Version: 1.1.2

Total installable skills: 112

## Packaging Notes

- Each skill is packaged as its own folder under `plugins/zeref-skills-fleet/skills/<skill-name>/SKILL.md`.
- Every `SKILL.md` starts with YAML frontmatter containing `name` and `description`.
- Skill names use lowercase kebab-case and match folder names.
- Claude Code plugin metadata is versioned in both `.claude-plugin/plugin.json` and root `.claude-plugin/marketplace.json`.
- Notion/Linear update blocks, token discipline, and anti-hallucination rules are embedded in every skill.


## Fleet Summary

| Fleet | Skill Count |
|---|---:|
| Zeref HQ | 8 |
| Business Team | 14 |
| UI/UX Team | 16 |
| Dev Team | 17 |
| Testing & Quality Team | 15 |
| Marketing Team | 16 |
| Content Writing & Creation Team | 16 |
| Final Compiler Layer | 4 |
| System Governance Layer | 6 |

## Skills

### Zeref HQ

| Skill | Title | Token Tier | Outputs |
|---|---|---|---|
| `zeref-hq-fleet-activator` | Zeref HQ Fleet Activator | M-L | `Fleet_Activation_Plan.md`, `Notion_Project_Update.md`, `Linear_Ticket_Plan.md` |
| `zeref-hq-chief-strategy-officer` | Chief Strategy Officer | L-XL | `Project_Strategy_Brief.md`, `Strategic_Options_Matrix.md`, `Decision_Log_Update.md` |
| `zeref-hq-chief-product-officer` | Chief Product Officer | L-XL | `Product_Direction_Document.md`, `MVP_Scope.md`, `Product_Roadmap.md` |
| `zeref-hq-chief-operating-officer` | Chief Operating Officer | M-L | `Operating_Plan.md`, `Execution_Rhythm.md`, `Linear_Workflow_Map.md` |
| `zeref-hq-chief-research-officer` | Chief Research Officer | L-XL | `Evidence_Validation_Report.md`, `Research_Gap_Log.md`, `Source_Quality_Matrix.md` |
| `zeref-hq-chief-of-staff` | Chief of Staff | M | `Project_Control_Brief.md`, `Dependency_Map.md`, `Status_Update.md` |
| `zeref-hq-documentation-architect` | Documentation Architect | M-L | `Documentation_Architecture_Plan.md`, `Folder_Map.md`, `File_Naming_Standards.md` |
| `zeref-hq-quality-gatekeeper` | HQ Quality Gatekeeper | XL | `Executive_QA_Report.md`, `Final_Blocker_List.md`, `Approval_Status.md` |

### Business Team

| Skill | Title | Token Tier | Outputs |
|---|---|---|---|
| `zeref-biz-business-strategist` | Business Strategist | L-XL | `Business_Strategy_Brief.md`, `Business_Model_Canvas.md` |
| `zeref-biz-market-research-analyst` | Market Research Analyst | L-XL | `Market_Research_Report.md`, `Trend_Analysis.md` |
| `zeref-biz-competitive-intelligence-analyst` | Competitive Intelligence Analyst | L | `Competitive_Analysis_Matrix.md`, `Differentiation_Report.md` |
| `zeref-biz-business-validator` | Business Validator | L-XL | `Business_Validation_Report.md`, `Go_No_Go_Memo.md` |
| `zeref-biz-product-market-fit-analyst` | Product-Market Fit Analyst | L | `PMF_Hypothesis_Report.md`, `Validation_Test_Plan.md` |
| `zeref-biz-financial-analyst` | Financial Analyst | M-L | `Financial_Model_Brief.md`, `Pricing_Assumptions.md` |
| `zeref-biz-monetization-strategist` | Monetization Strategist | L | `Monetization_Strategy.md`, `Pricing_Options_Matrix.md` |
| `zeref-biz-operations-strategist` | Operations Strategist | M-L | `Operations_Blueprint.md`, `SOP_Index.md` |
| `zeref-biz-risk-analyst` | Risk Analyst | L-XL | `Risk_Register.md`, `Mitigation_Plan.md` |
| `zeref-biz-legal-advisor` | Legal Advisor | XL | `Legal_Risk_Memo.md`, `Compliance_Checklist.md` |
| `zeref-biz-partnership-strategist` | Partnership Strategist | M-L | `Partnership_Strategy.md`, `Partner_Target_List.md` |
| `zeref-biz-investor-pitch-strategist` | Investor Pitch Strategist | L-XL | `Investor_Memo.md`, `Pitch_Deck_Outline.md` |
| `zeref-biz-grant-funding-analyst` | Grant/Funding Analyst | M-L | `Funding_Opportunity_Report.md`, `Application_Materials_Checklist.md` |
| `zeref-biz-kpi-analyst` | Business KPI Analyst | M | `KPI_Framework.md`, `Metrics_Dictionary.md` |

### UI/UX Team

| Skill | Title | Token Tier | Outputs |
|---|---|---|---|
| `zeref-ux-research-lead` | UX Research Lead | L-XL | `User_Research_Plan.md`, `Interview_Script.md`, `Survey_Plan.md` |
| `zeref-ux-synthetic-research-analyst` | Synthetic Research Analyst | M-L | `Synthetic_Research_Findings.md`, `Affinity_Map.md`, `User_Insights.md` |
| `zeref-ux-persona-strategist` | User Persona Strategist | M-L | `Personas.md`, `User_Scenarios.md`, `JTBD_Framework.md` |
| `zeref-ux-problem-definition-specialist` | Problem Definition Specialist | L | `Problem_Definition.md`, `HMW_Statements.md`, `Design_Challenge.md` |
| `zeref-ux-information-architect` | Information Architect | M-L | `Information_Architecture.md`, `Sitemap.md`, `Navigation_Model.md` |
| `zeref-ux-user-flow-designer` | User Flow Designer | M-L | `User_Flows.md`, `Journey_Map.md`, `Edge_Flow_Map.md` |
| `zeref-ux-product-designer` | Product Designer | L | `Screen_Requirements.md`, `Product_UX_Spec.md`, `State_Model.md` |
| `zeref-ux-interaction-designer` | Interaction Designer | M | `Interaction_Guidelines.md`, `Motion_And_Feedback_Rules.md` |
| `zeref-ux-visual-designer` | Visual Designer | M | `Visual_Direction.md`, `UI_Style_Notes.md` |
| `zeref-ux-design-systems-architect` | Design Systems Architect | L | `Design_System_Specification.md`, `Component_Library_Guide.md`, `Token_Dictionary.md` |
| `zeref-ux-accessibility-specialist` | Accessibility Specialist | L | `Accessibility_Audit.md`, `Accessibility_Fix_List.md` |
| `zeref-ux-writer` | UX Writer | S-M | `UX_Copy_System.md`, `Microcopy_Table.md` |
| `zeref-ux-prototype-specialist` | Prototype Specialist | M | `Prototype_Readiness_Report.md`, `Prototype_Flow_Checklist.md` |
| `zeref-ux-figma-architecture-specialist` | Figma Architecture Specialist | M-L | `Figma_Architecture_Plan.md`, `Figma_Cleanup_Checklist.md` |
| `zeref-ux-developer-handoff-lead` | Developer Handoff Lead | L-XL | `Dev_Handoff.md`, `Component_Handoff.md`, `Screen_State_Spec.md` |
| `zeref-ux-design-qa-auditor` | Design QA Auditor | L | `Design_QA_Report.md`, `Design_Issue_Log.md` |

### Dev Team

| Skill | Title | Token Tier | Outputs |
|---|---|---|---|
| `zeref-dev-technical-architect` | Technical Architect | XL | `Technical_Architecture.md`, `System_Diagram_Notes.md` |
| `zeref-dev-solution-architect` | Solution Architect | L-XL | `Solution_Design.md`, `Implementation_Phases.md` |
| `zeref-dev-frontend-engineer` | Frontend Engineer | M-L | `Frontend_Implementation_Plan.md`, `Frontend_Component_Map.md` |
| `zeref-dev-ios-engineer` | Mobile iOS Engineer | M-L | `iOS_Build_Plan.md`, `SwiftUI_Architecture.md` |
| `zeref-dev-android-engineer` | Mobile Android Engineer | M-L | `Android_Build_Plan.md`, `Compose_Architecture.md` |
| `zeref-dev-fullstack-engineer` | Full-Stack Engineer | L-XL | `Full_Stack_Implementation_Plan.md`, `Integration_Map.md` |
| `zeref-dev-backend-engineer` | Backend Engineer | L | `Backend_Architecture.md`, `API_Endpoint_Spec.md` |
| `zeref-dev-database-architect` | Database Architect | L | `Data_Model.md`, `Schema_Dictionary.md`, `Sample_Records.md` |
| `zeref-dev-firebase-specialist` | Firebase Specialist | M-L | `Firebase_Setup_Guide.md`, `Firestore_Rules_Notes.md` |
| `zeref-dev-mongodb-specialist` | MongoDB Specialist | M-L | `MongoDB_Schema_Guide.md`, `Mongo_Query_Patterns.md` |
| `zeref-dev-api-integration-engineer` | API Integration Engineer | L | `API_Integration_Notes.md`, `External_Service_Map.md` |
| `zeref-dev-ai-systems-engineer` | AI Systems Engineer | XL | `AI_Logic_Specification.md`, `Prompt_Architecture.md`, `AI_Evaluation_Plan.md` |
| `zeref-dev-security-engineer` | Security Engineer | XL | `Security_Audit.md`, `Security_Fix_Plan.md` |
| `zeref-dev-devops-engineer` | DevOps Engineer | M-L | `Deployment_Plan.md`, `Release_Checklist.md` |
| `zeref-dev-code-quality-reviewer` | Code Quality Reviewer | L-XL | `Code_Review_Report.md`, `Refactor_Priority_List.md` |
| `zeref-dev-github-repository-manager` | GitHub Repository Manager | M | `GitHub_Repo_Blueprint.md`, `Branching_Strategy.md` |
| `zeref-dev-technical-documentation-writer` | Technical Documentation Writer | S-M | `README.md`, `Setup_Guide.md`, `Technical_Documentation.md` |

### Testing & Quality Team

| Skill | Title | Token Tier | Outputs |
|---|---|---|---|
| `zeref-qa-lead` | QA Lead | L-XL | `QA_Strategy.md`, `Quality_Gates.md` |
| `zeref-qa-ux-usability-tester` | UX Usability Tester | L | `Usability_Test_Plan.md`, `Usability_Findings_Report.md` |
| `zeref-qa-ui-consistency-auditor` | UI Consistency Auditor | M | `UI_Consistency_Audit.md`, `Visual_Fix_List.md` |
| `zeref-qa-accessibility-tester` | Accessibility Tester | L | `Accessibility_QA_Report.md`, `Accessibility_Retest_Checklist.md` |
| `zeref-qa-functional-tester` | Functional QA Tester | M-L | `Functional_Test_Cases.md`, `Bug_Report.md` |
| `zeref-qa-regression-tester` | Regression Tester | M | `Regression_Checklist.md`, `Regression_Result_Log.md` |
| `zeref-qa-edge-case-tester` | Edge Case Tester | L | `Edge_Case_Report.md`, `Failure_State_Checklist.md` |
| `zeref-qa-performance-tester` | Performance Tester | M-L | `Performance_Report.md`, `Optimization_Backlog.md` |
| `zeref-qa-security-tester` | Security QA Tester | XL | `Security_QA_Report.md`, `Security_Retest_Checklist.md` |
| `zeref-qa-analytics-specialist` | Analytics QA Specialist | M | `Analytics_QA_Checklist.md`, `Tracking_Issue_Log.md` |
| `zeref-qa-ab-testing-strategist` | A/B Testing Strategist | L | `AB_Test_Plan.md`, `Experiment_Backlog.md` |
| `zeref-qa-marketing-auditor` | Marketing QA Auditor | M-L | `Marketing_QA_Report.md`, `Funnel_Issue_Log.md` |
| `zeref-qa-launch-readiness-manager` | Launch Readiness Manager | XL | `Launch_Readiness_Checklist.md`, `Launch_Blocker_List.md` |
| `zeref-qa-rubric-alignment-auditor` | Rubric Alignment Auditor | L-XL | `Rubric_Compliance_Report.md`, `Rubric_Fix_Plan.md` |
| `zeref-qa-final-quality-gatekeeper` | Final Quality Gatekeeper | XL-XXL | `Final_QA_Signoff.md`, `Final_Fix_List.md` |

### Marketing Team

| Skill | Title | Token Tier | Outputs |
|---|---|---|---|
| `zeref-mkt-chief-marketing-strategist` | Chief Marketing Strategist | L-XL | `Marketing_Strategy.md`, `Marketing_Roadmap.md` |
| `zeref-mkt-brand-strategist` | Brand Strategist | L | `Brand_Strategy_Guide.md`, `Messaging_Pillars.md` |
| `zeref-mkt-positioning-strategist` | Positioning Strategist | L | `Positioning_Brief.md`, `Positioning_Statement.md` |
| `zeref-mkt-gtm-strategist` | GTM Strategist | L-XL | `GTM_Plan.md`, `Launch_Channel_Plan.md` |
| `zeref-mkt-seo-strategist` | SEO Strategist | L | `SEO_Strategy.md`, `Keyword_Map.md`, `Metadata_Plan.md` |
| `zeref-mkt-content-marketing-strategist` | Content Marketing Strategist | M-L | `Content_Marketing_Plan.md`, `Content_Calendar.md` |
| `zeref-mkt-social-media-strategist` | Social Media Strategist | M-L | `Social_Media_Strategy.md`, `Social_Content_Calendar.md` |
| `zeref-mkt-performance-marketing-specialist` | Performance Marketing Specialist | L | `Paid_Media_Strategy.md`, `Campaign_Test_Plan.md` |
| `zeref-mkt-affiliate-marketing-strategist` | Affiliate Marketing Strategist | M-L | `Affiliate_Strategy.md`, `Referral_Program_Plan.md` |
| `zeref-mkt-email-marketing-specialist` | Email Marketing Specialist | M | `Email_Marketing_Strategy.md`, `Lifecycle_Email_Map.md` |
| `zeref-mkt-growth-marketer` | Growth Marketer | L | `Growth_Experiment_Plan.md`, `Growth_Backlog.md` |
| `zeref-mkt-conversion-rate-optimizer` | Conversion Rate Optimizer | L | `CRO_Audit.md`, `Conversion_Test_Plan.md` |
| `zeref-mkt-analytics-specialist` | Marketing Analytics Specialist | M-L | `Marketing_Analytics_Plan.md`, `Dashboard_Spec.md` |
| `zeref-mkt-community-strategist` | Community Strategist | M | `Community_Growth_Plan.md`, `Community_Operations_Guide.md` |
| `zeref-mkt-pr-communications-specialist` | PR & Communications Specialist | L | `PR_Messaging_Kit.md`, `Announcement_Brief.md` |
| `zeref-mkt-personal-branding-strategist` | Personal Branding Strategist | L-XL | `Personal_Brand_Strategy.md`, `Profile_Optimization_Plan.md` |

### Content Writing & Creation Team

| Skill | Title | Token Tier | Outputs |
|---|---|---|---|
| `zeref-cnt-editorial-director` | Editorial Director | L | `Editorial_Strategy.md`, `Publishing_Standards.md` |
| `zeref-cnt-copywriter` | Copywriter | S-M | `Copywriting_Drafts.md`, `CTA_Variants.md` |
| `zeref-cnt-ux-case-study-writer` | UX Case Study Writer | L-XL | `UX_Case_Study.md`, `Case_Study_Outline.md` |
| `zeref-cnt-technical-case-study-writer` | Technical Case Study Writer | L | `Technical_Case_Study.md`, `Dev_Project_Writeup.md` |
| `zeref-cnt-long-form-writer` | Long-Form Writer | M-L | `Long_Form_Draft.md`, `Article_Outline.md` |
| `zeref-cnt-linkedin-ghostwriter` | LinkedIn Ghostwriter | S-M | `LinkedIn_Content_Pack.md`, `LinkedIn_Post_Drafts.md` |
| `zeref-cnt-scriptwriter` | Scriptwriter | S-M | `Video_Script.md`, `Demo_Narration.md` |
| `zeref-cnt-presentation-designer` | Presentation Designer | M-L | `Presentation_Outline.md`, `Slide_Content_Draft.md` |
| `zeref-cnt-visual-asset-prompt-engineer` | Visual Asset Prompt Engineer | S-M | `Visual_Prompt_Library.md`, `Asset_Direction_Brief.md` |
| `zeref-cnt-video-content-strategist` | Video Content Strategist | M | `Video_Content_Plan.md`, `Video_Series_Map.md` |
| `zeref-cnt-repurposing-specialist` | Content Repurposing Specialist | S-M | `Repurposing_Matrix.md`, `Channel_Content_Map.md` |
| `zeref-cnt-seo-content-writer` | SEO Content Writer | M | `SEO_Content_Draft.md`, `Metadata_Drafts.md` |
| `zeref-cnt-documentation-writer` | Documentation Writer | M | `Documentation_File.md`, `SOP_Document.md` |
| `zeref-cnt-resume-career-writer` | Resume & Career Writer | M-L | `Resume_Draft.md`, `Cover_Letter_Draft.md`, `Recruiter_Message.md` |
| `zeref-cnt-brand-voice-editor` | Brand Voice Editor | S-M | `Voice_Tone_Audit.md`, `Polished_Copy.md` |
| `zeref-cnt-content-qa-editor` | Content QA Editor | S-M | `Final_Edited_Copy.md`, `Content_QA_Report.md` |

### Final Compiler Layer

| Skill | Title | Token Tier | Outputs |
|---|---|---|---|
| `zeref-final-project-compiler` | Project Compiler | XXL | `Final_Project_Index.md`, `Compiled_Project_Report.md`, `Handoff_Summary.md` |
| `zeref-final-source-validator` | Source Validator | XL | `Source_Validation_Report.md`, `Evidence_Gap_Log.md` |
| `zeref-final-deliverable-packager` | Deliverable Packager | XL | `Deliverable_Packaging_Plan.md`, `Export_Checklist.md`, `Final_Folder_Map.md` |
| `zeref-final-executive-reviewer` | Executive Reviewer | XL-XXL | `Executive_Final_Review.md`, `Approval_Decision.md`, `Next_Action_Memo.md` |

### System Governance Layer

| Skill | Title | Token Tier | Outputs |
|---|---|---|---|
| `zeref-system-skill-router` | System Skill Router | M | `Skill_Routing_Decision.md`, `Stack_Selection_Table.md` |
| `zeref-system-caveman-compressor` | Caveman Compressor | S-M | `Compressed_Context_Brief.md`, `Constraint_Preservation_Log.md` |
| `zeref-system-token-budget-controller` | Token Budget Controller | S-M | `Token_Budget_Plan.md`, `Context_Loading_Map.md` |
| `zeref-system-evidence-memory-keeper` | Evidence Memory Keeper | M-L | `Evidence_Memory_Log.md`, `Decision_Register.md` |
| `zeref-system-marketplace-packager` | Marketplace Packager | L | `Marketplace_Package_Map.md`, `Release_Checklist.md`, `Validation_Report.json` |
| `zeref-system-plugin-update-diagnostician` | Plugin Update Diagnostician | M | `Plugin_Update_Diagnosis.md`, `Fix_Command_List.md` |
