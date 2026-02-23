# Spec and build

## Agent Instructions

Ask the user questions when anything is unclear or needs their input. This includes:

- Ambiguous or incomplete requirements
- Technical decisions that affect architecture or user experience
- Trade-offs that require business context

Do not make assumptions on important decisions — get clarification first.

---

## Workflow Steps

### [x] Step: Technical Specification

Assess the task's difficulty, as underestimating it leads to poor outcomes.

- easy: Straightforward implementation, trivial bug fix or feature
- medium: Moderate complexity, some edge cases or caveats to consider
- hard: Complex logic, many caveats, architectural considerations, or high-risk changes

Create a technical specification for the task that is appropriate for the complexity level:

- Review the existing codebase architecture and identify reusable components.
- Define the implementation approach based on established patterns in the project.
- Identify all source code files that will be created or modified.
- Define any necessary data model, API, or interface changes.
- Describe verification steps using the project's test and lint commands.

Save the output to `/Users/shreyash/Documents/Shreyash AI/.zencoder/chats/0a3bbe43-e0ff-42ee-a787-df7e57f1e862/spec.md` with:

- Technical context (language, dependencies)
- Implementation approach
- Source code structure changes
- Data model / API / interface changes
- Verification approach

If the task is complex enough, create a detailed implementation plan based on `/Users/shreyash/Documents/Shreyash AI/.zencoder/chats/0a3bbe43-e0ff-42ee-a787-df7e57f1e862/spec.md`:

- Break down the work into concrete tasks (incrementable, testable milestones)
- Each task should reference relevant contracts and include verification steps
- Replace the Implementation step below with the planned tasks

Rule of thumb for step size: each step should represent a coherent unit of work (e.g., implement a component, add an API endpoint, write tests for a module). Avoid steps that are too granular (single function).

Save to `/Users/shreyash/Documents/Shreyash AI/.zencoder/chats/0a3bbe43-e0ff-42ee-a787-df7e57f1e862/plan.md`. If the feature is trivial and doesn't warrant this breakdown, keep the Implementation step below as is.

---

### [ ] Step: Implementation

1. Update `llm_ollama.py` to support `BaseMessage` and `List[BaseMessage]`.
2. Update `prompt.py` to provide a system prompt instead of a single string.
3. Modify `ChatAgent` in `agent.py` to include `self.history` and manage conversation flow.
4. Verify by running the server and sending sequential queries.
5. Create `report.md`.
