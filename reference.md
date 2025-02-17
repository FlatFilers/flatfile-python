# Reference
## Accounts
<details><summary><code>client.accounts.<a href="src/flatfile/accounts/client.py">get_current</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the current account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.accounts.get_current()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/flatfile/accounts/client.py">update_current</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the current account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.accounts.update_current(
    default_app_id="us_app_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**default_app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Actions
<details><summary><code>client.actions.<a href="src/flatfile/actions/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.actions.create(
    space_id="spaceId",
    target_id="targetId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `SpaceId` — The Space ID for which to create the Action.
    
</dd>
</dl>

<dl>
<dd>

**target_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**label:** `str` — The text on the Button itself
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` — **This is deprecated. Use `operation` instead.**
    
</dd>
</dl>

<dl>
<dd>

**operation:** `typing.Optional[str]` — This will become the job operation that is triggered
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[ActionMode]` — Foreground and toolbarBlocking action mode will prevent interacting with the resource until complete
    
</dd>
</dl>

<dl>
<dd>

**tooltip:** `typing.Optional[str]` — A tooltip that appears when hovering the action button
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Optional[typing.Sequence[ActionMessage]]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — **This is deprecated.**
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The text that appears in the dialog after the action is clicked.
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[ActionSchedule]` — Determines if the action should happen on a regular cadence.
    
</dd>
</dl>

<dl>
<dd>

**primary:** `typing.Optional[bool]` — A primary action will be more visibly present, whether in Sheet or Workbook.
    
</dd>
</dl>

<dl>
<dd>

**confirm:** `typing.Optional[bool]` — Whether to show a modal to confirm the action
    
</dd>
</dl>

<dl>
<dd>

**icon:** `typing.Optional[str]` — Icon will work on primary actions. It will only accept an already existing Flatfile design system icon.
    
</dd>
</dl>

<dl>
<dd>

**require_all_valid:** `typing.Optional[bool]` — **This is deprecated. Use `constraints` instead.**
    
</dd>
</dl>

<dl>
<dd>

**require_selection:** `typing.Optional[bool]` — **This is deprecated. Use `constraints` instead.**
    
</dd>
</dl>

<dl>
<dd>

**input_form:** `typing.Optional[InputForm]` — Adds an input form for this action after it is clicked.
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[typing.Sequence[ActionConstraint]]` — A limitation or restriction on the action.
    
</dd>
</dl>

<dl>
<dd>

**mount:** `typing.Optional[ActionMount]` 
    
</dd>
</dl>

<dl>
<dd>

**guide:** `typing.Optional[Guide]` 
    
</dd>
</dl>

<dl>
<dd>

**guardrail:** `typing.Optional[Guardrail]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/flatfile/actions/client.py">bulk_create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile
from flatfile.commons import ApiActionConfig

client = Flatfile(
    token="YOUR_TOKEN",
)
client.actions.bulk_create(
    space_id="spaceId",
    request=[
        ApiActionConfig(
            target_id="targetId",
        ),
        ApiActionConfig(
            target_id="targetId",
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `SpaceId` — The Space ID for which to create the Actions.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ApiActionConfigs` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/flatfile/actions/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.actions.get_all(
    space_id="spaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `SpaceId` — The Space ID for which to get the Actions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/flatfile/actions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.actions.get(
    action_id="actionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action_id:** `ActionId` — The id of the action to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/flatfile/actions/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.actions.update(
    action_id="actionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action_id:** `ActionId` — The id of the action to patch
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` — **This is deprecated. Use `operation` instead.**
    
</dd>
</dl>

<dl>
<dd>

**operation:** `typing.Optional[str]` — This will become the job operation that is triggered
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[ActionMode]` — Foreground and toolbarBlocking action mode will prevent interacting with the resource until complete
    
</dd>
</dl>

<dl>
<dd>

**tooltip:** `typing.Optional[str]` — A tooltip that appears when hovering the action button
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Optional[typing.Sequence[ActionMessage]]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — **This is deprecated.**
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The text that appears in the dialog after the action is clicked.
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[ActionSchedule]` — Determines if the action should happen on a regular cadence.
    
</dd>
</dl>

<dl>
<dd>

**primary:** `typing.Optional[bool]` — A primary action will be more visibly present, whether in Sheet or Workbook.
    
</dd>
</dl>

<dl>
<dd>

**confirm:** `typing.Optional[bool]` — Whether to show a modal to confirm the action
    
</dd>
</dl>

<dl>
<dd>

**icon:** `typing.Optional[str]` — Icon will work on primary actions. It will only accept an already existing Flatfile design system icon.
    
</dd>
</dl>

<dl>
<dd>

**require_all_valid:** `typing.Optional[bool]` — **This is deprecated. Use `constraints` instead.**
    
</dd>
</dl>

<dl>
<dd>

**require_selection:** `typing.Optional[bool]` — **This is deprecated. Use `constraints` instead.**
    
</dd>
</dl>

<dl>
<dd>

**input_form:** `typing.Optional[InputForm]` — Adds an input form for this action after it is clicked.
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[typing.Sequence[ActionConstraint]]` — A limitation or restriction on the action.
    
</dd>
</dl>

<dl>
<dd>

**mount:** `typing.Optional[ActionMount]` 
    
</dd>
</dl>

<dl>
<dd>

**guide:** `typing.Optional[Guide]` 
    
</dd>
</dl>

<dl>
<dd>

**guardrail:** `typing.Optional[Guardrail]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/flatfile/actions/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.actions.delete(
    action_id="actionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action_id:** `ActionId` — The id of the action to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AgentExports
<details><summary><code>client.agent_exports.<a href="src/flatfile/agent_exports/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.agent_exports.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `typing.Optional[EnvironmentId]` 
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[AgentId]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[PageSize]` 
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[PageNumber]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent_exports.<a href="src/flatfile/agent_exports/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.agent_exports.get(
    agent_export_id="us_agx_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_export_id:** `AgentExportId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent_exports.<a href="src/flatfile/agent_exports/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.agent_exports.delete(
    agent_export_id="us_agx_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_export_id:** `AgentExportId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agents
<details><summary><code>client.agents.<a href="src/flatfile/agents/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.agents.list(
    environment_id="us_env_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `EnvironmentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/flatfile/agents/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.agents.create(
    environment_id="us_env_YOUR_ID",
    topics=["workbook:updated"],
    compiler="js",
    source="module.exports = { routeEvent: async (...args) => { console.log(args) } }",
    options={"namespace": "space:blue"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `EnvironmentId` 
    
</dd>
</dl>

<dl>
<dd>

**topics:** `typing.Optional[typing.Sequence[EventTopic]]` — The topics the agent should listen for
    
</dd>
</dl>

<dl>
<dd>

**compiler:** `typing.Optional[Compiler]` — The compiler of the agent
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[str]` — The source of the agent
    
</dd>
</dl>

<dl>
<dd>

**source_map:** `typing.Optional[str]` — The source map of the agent
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` — The slug of the agent
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Options for the agent
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/flatfile/agents/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.agents.get(
    agent_id="us_ag_YOUR_ID",
    environment_id="us_env_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `AgentId` 
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `typing.Optional[EnvironmentId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/flatfile/agents/client.py">list_versions</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.agents.list_versions(
    agent_id="agentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `AgentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/flatfile/agents/client.py">revert</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.agents.revert(
    agent_id="agentId",
    agent_version_id="agentVersionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `AgentId` 
    
</dd>
</dl>

<dl>
<dd>

**agent_version_id:** `AgentVersionId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/flatfile/agents/client.py">list_agent_roles</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists roles assigned to an agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.agents.list_agent_roles(
    agent_id="agentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `AgentId` — The agent id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/flatfile/agents/client.py">assign_agent_role</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Assigns a role to a agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.agents.assign_agent_role(
    agent_id="agentId",
    role_id="roleId",
    resource_id="resourceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `AgentId` — The agent id
    
</dd>
</dl>

<dl>
<dd>

**role_id:** `RoleId` 
    
</dd>
</dl>

<dl>
<dd>

**resource_id:** `ResourceIdUnion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/flatfile/agents/client.py">delete_agent_role</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a role from an agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.agents.delete_agent_role(
    agent_id="agentId",
    actor_role_id="actorRoleId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `AgentId` — The agent id
    
</dd>
</dl>

<dl>
<dd>

**actor_role_id:** `ActorRoleId` — The actor role id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/flatfile/agents/client.py">get_agent_logs</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.agents.get_agent_logs(
    agent_id="us_ag_YOUR_ID",
    environment_id="us_env_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `AgentId` 
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `EnvironmentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/flatfile/agents/client.py">get_agent_log</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.agents.get_agent_log(
    event_id="commons.EventId",
    environment_id="us_env_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**event_id:** `EventId` 
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `EnvironmentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/flatfile/agents/client.py">get_environment_agent_logs</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.agents.get_environment_agent_logs(
    environment_id="us_env_YOUR_ID",
    space_id="us_sp_YOUR_ID",
    success=True,
    page_size=20,
    page_number=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `EnvironmentId` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[SpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**success:** `typing.Optional[SuccessQueryParameter]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[PageSize]` 
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[PageNumber]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/flatfile/agents/client.py">get_environment_agent_executions</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.agents.get_environment_agent_executions(
    environment_id="us_env_YOUR_ID",
    agent_id="us_ag_YOUR_ID",
    space_id="us_sp_YOUR_ID",
    success=True,
    page_size=20,
    page_number=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `EnvironmentId` 
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[AgentId]` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[SpaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**success:** `typing.Optional[SuccessQueryParameter]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[PageSize]` 
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[PageNumber]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/flatfile/agents/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a single agent
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.agents.delete(
    agent_id="us_ag_YOUR_ID",
    environment_id="us_env_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `AgentId` 
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `EnvironmentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Apps
<details><summary><code>client.apps.<a href="src/flatfile/apps/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns apps in an account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.apps.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apps.<a href="src/flatfile/apps/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an app
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.apps.get(
    app_id="us_app_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_id:** `AppId` — ID of app
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apps.<a href="src/flatfile/apps/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an app
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.apps.update(
    app_id="us_app_YOUR_ID",
    name="Nightly Data Loads",
    namespace="nightly-data",
    entity="Sync",
    entity_plural="Syncs",
    icon='<svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-bar-chart-fill" viewBox="0 0 16 16">\n  <path d="M1 11a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1zm5-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1z"/>\n</svg>',
    metadata={"foo": "bar"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_id:** `AppId` — ID of app
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**entity:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**entity_plural:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**icon:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**environment_filters:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**blueprint:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**activated_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apps.<a href="src/flatfile/apps/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an app
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.apps.create(
    name="Nightly Data Loads",
    namespace="nightly-data",
    type="CUSTOM",
    entity="Sync",
    entity_plural="Syncs",
    icon='<svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-bar-chart-fill" viewBox="0 0 16 16">\n  <path d="M1 11a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1zm5-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1z"/>\n</svg>',
    metadata={"foo": "bar"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `AppType` 
    
</dd>
</dl>

<dl>
<dd>

**entity:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**entity_plural:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**icon:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**environment_filters:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**blueprint:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apps.<a href="src/flatfile/apps/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an app
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.apps.delete(
    app_id="us_app_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_id:** `AppId` — ID of app to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apps.<a href="src/flatfile/apps/client.py">get_constraints</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns constraints for an app
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.apps.get_constraints(
    app_id="appId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_id:** `AppId` — ID of the app
    
</dd>
</dl>

<dl>
<dd>

**include_builtins:** `typing.Optional[bool]` — Whether to include built-in constraints
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apps.<a href="src/flatfile/apps/client.py">create_constraint</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new constraint for an app
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.apps.create_constraint(
    app_id_="appId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_id_:** `AppId` — ID of the app
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**function:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**validator:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `typing.Optional[AppId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apps.<a href="src/flatfile/apps/client.py">get_constraint_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a specific constraint
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.apps.get_constraint_by_id(
    app_id="appId",
    constraint_id="constraintId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_id:** `AppId` — ID of the app
    
</dd>
</dl>

<dl>
<dd>

**constraint_id:** `ConstraintId` — ID of the constraint
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apps.<a href="src/flatfile/apps/client.py">get_constraint_versions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the versions of a specific constraint
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.apps.get_constraint_versions(
    app_id="appId",
    constraint_id="constraintId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_id:** `AppId` — ID of the app
    
</dd>
</dl>

<dl>
<dd>

**constraint_id:** `ConstraintId` — ID of the constraint
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apps.<a href="src/flatfile/apps/client.py">get_constraint_version</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a specified version of a specific constraint
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.apps.get_constraint_version(
    app_id="appId",
    constraint_id="constraintId",
    version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_id:** `AppId` — ID of the app
    
</dd>
</dl>

<dl>
<dd>

**constraint_id:** `ConstraintId` — ID of the constraint
    
</dd>
</dl>

<dl>
<dd>

**version:** `int` — Version of the constraint
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apps.<a href="src/flatfile/apps/client.py">update_constraint</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a specific constraint
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.apps.update_constraint(
    app_id="appId",
    constraint_id="constraintId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_id:** `AppId` — ID of the app
    
</dd>
</dl>

<dl>
<dd>

**constraint_id:** `ConstraintId` — ID of the constraint
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**function:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apps.<a href="src/flatfile/apps/client.py">delete_constraint</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a specific constraint
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.apps.delete_constraint(
    app_id="appId",
    constraint_id="constraintId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_id:** `AppId` — ID of the app
    
</dd>
</dl>

<dl>
<dd>

**constraint_id:** `ConstraintId` — ID of the constraint
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Assistant
<details><summary><code>client.assistant.<a href="src/flatfile/assistant/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns prompts created by user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.assistant.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt_type:** `typing.Optional[PromptTypeQueryEnum]` — Type of prompt (default AI_ASSIST)
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of prompts to return in a page (default 7)
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Based on pageSize, which page of prompts to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assistant.<a href="src/flatfile/assistant/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a prompt
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.assistant.get(
    prompt_id="us_pr_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt_id:** `PromptId` — ID of prompts
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assistant.<a href="src/flatfile/assistant/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a prompt
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.assistant.update(
    prompt_id="us_pr_YOUR_ID",
    prompt="Combine first name and last name into a new column called Full Name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt_id:** `PromptId` — ID of prompts
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assistant.<a href="src/flatfile/assistant/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a prompt
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.assistant.create(
    prompt="Combine first name and last name into a new column called Full Name",
    environment_id="us_env_YOUR_ID",
    space_id="us_sp_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `EnvironmentId` 
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `SpaceId` 
    
</dd>
</dl>

<dl>
<dd>

**prompt_type:** `typing.Optional[PromptTypeEnum]` — Type of prompt; Defaults to AI_ASSIST
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assistant.<a href="src/flatfile/assistant/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a prompts
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.assistant.delete(
    prompt_id="us_pr_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt_id:** `PromptId` — ID of prompts
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Auth
<details><summary><code>client.auth.<a href="src/flatfile/auth/client.py">get_sftp_credentials</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.auth.get_sftp_credentials(
    space_id="spaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `SpaceId` — ID of space to get credentials for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Commits
<details><summary><code>client.commits.<a href="src/flatfile/commits/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details of a commit version
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.commits.get(
    commit_id="us_vr_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**commit_id:** `CommitId` — ID of the commit version to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.commits.<a href="src/flatfile/commits/client.py">complete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Completes a commit version. This marks the commit as complete and acknowledges that the changes have been applied to the sheet.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.commits.complete(
    commit_id="commitId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**commit_id:** `CommitId` — ID of the commit version to complete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.commits.<a href="src/flatfile/commits/client.py">replay</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replays a commit:created event.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.commits.replay(
    commit_id="commitId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**commit_id:** `CommitId` — ID of the commit version to re-emit a commit:created event for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DataRetentionPolicies
<details><summary><code>client.data_retention_policies.<a href="src/flatfile/data_retention_policies/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all data retention policies on an account matching a filter for environmentId
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.data_retention_policies.list(
    environment_id="us_env_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `typing.Optional[EnvironmentId]` — The associated Environment ID of the policy.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_retention_policies.<a href="src/flatfile/data_retention_policies/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new data retention policy to the space
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.data_retention_policies.create(
    type="lastActivity",
    period=5,
    environment_id="us_env_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `DataRetentionPolicyEnum` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `EnvironmentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_retention_policies.<a href="src/flatfile/data_retention_policies/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single data retention policy
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.data_retention_policies.get(
    id="us_drp_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `DataRetentionPolicyId` — ID of data retention policy to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_retention_policies.<a href="src/flatfile/data_retention_policies/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a single data retention policy
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.data_retention_policies.update(
    id="us_drp_YOUR_ID",
    type="lastActivity",
    period=5,
    environment_id="us_env_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `DataRetentionPolicyId` — ID of data retention policy to update
    
</dd>
</dl>

<dl>
<dd>

**type:** `DataRetentionPolicyEnum` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `EnvironmentId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_retention_policies.<a href="src/flatfile/data_retention_policies/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a single data retention policy
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.data_retention_policies.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `DataRetentionPolicyId` — ID of data retention policy to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Documents
<details><summary><code>client.documents.<a href="src/flatfile/documents/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all documents for a space
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.documents.list(
    space_id="us_sp_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `SpaceId` — ID of space to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/flatfile/documents/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new document to the space
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile
from flatfile.commons import Action

client = Flatfile(
    token="YOUR_TOKEN",
)
client.documents.create(
    space_id="us_sp_YOUR_ID",
    title="My Document 1",
    body="My information",
    actions=[
        Action(
            operation="submitAction",
            mode="foreground",
            label="Submit",
            description="Submit data to webhook.site",
            primary=True,
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `SpaceId` — ID of space to return
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**treatments:** `typing.Optional[typing.Sequence[str]]` — Certain treatments will cause your Document to look or behave differently.
    
</dd>
</dl>

<dl>
<dd>

**actions:** `typing.Optional[typing.Sequence[Action]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/flatfile/documents/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single document
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.documents.get(
    space_id="us_sp_YOUR_ID",
    document_id="us_dc_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `SpaceId` — ID of space to return
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `DocumentId` — ID of document to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/flatfile/documents/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

updates a single document, for only the body and title
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.documents.update(
    space_id="us_sp_YOUR_ID",
    document_id="us_dc_YOUR_ID",
    title="Updated Title",
    body="Updated My information",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `SpaceId` — ID of space to return
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `DocumentId` — ID of document to return
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**treatments:** `typing.Optional[typing.Sequence[str]]` — Certain treatments will cause your Document to look or behave differently.
    
</dd>
</dl>

<dl>
<dd>

**actions:** `typing.Optional[typing.Sequence[Action]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/flatfile/documents/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a single document
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.documents.delete(
    space_id="spaceId",
    document_id="documentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `SpaceId` — ID of space to return
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `DocumentId` — ID of document to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entitlements
<details><summary><code>client.entitlements.<a href="src/flatfile/entitlements/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all entitlements matching a filter for resourceId
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.entitlements.list(
    resource_id="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**resource_id:** `str` — The associated Resource ID for the entitlements.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Environments
<details><summary><code>client.environments.<a href="src/flatfile/environments/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all environments
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.environments.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of environments to return in a page (default 10)
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Based on pageSize, which page of environments to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/flatfile/environments/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new environment
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.environments.create(
    name="dev",
    is_prod=False,
    guest_authentication=["magic_link"],
    metadata={"key": "value"},
    namespaces=["default"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the environment
    
</dd>
</dl>

<dl>
<dd>

**is_prod:** `bool` — Whether or not the environment is a production environment
    
</dd>
</dl>

<dl>
<dd>

**guest_authentication:** `typing.Optional[typing.Sequence[GuestAuthenticationEnum]]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**translations_path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**namespaces:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**language_override:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/flatfile/environments/client.py">get_environment_event_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a token which can be used to subscribe to events for this environment
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.environments.get_environment_event_token(
    environment_id="us_env_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `EnvironmentId` — ID of environment to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/flatfile/environments/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single environment
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.environments.get(
    environment_id="us_env_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` — ID of the environment to return. To fetch the current environment, pass `current`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/flatfile/environments/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a single environment, to change the name for example
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.environments.update(
    environment_id="us_env_YOUR_ID",
    name="dev",
    is_prod=False,
    guest_authentication=["magic_link"],
    metadata={"key": "value"},
    namespaces=["default"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` — ID of the environment to update
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the environment
    
</dd>
</dl>

<dl>
<dd>

**is_prod:** `typing.Optional[bool]` — Whether or not the environment is a production environment
    
</dd>
</dl>

<dl>
<dd>

**guest_authentication:** `typing.Optional[typing.Sequence[GuestAuthenticationEnum]]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**translations_path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**namespaces:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**language_override:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/flatfile/environments/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a single environment
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.environments.delete(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` — ID of the environment to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/flatfile/environments/client.py">list_guides</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns guides in an account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.environments.list_guides(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `EnvironmentId` — ID of the environment
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/flatfile/environments/client.py">get_guide</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a guide
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.environments.get_guide(
    environment_id="us_env_YOUR_ID",
    guide_id="us_gu_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `EnvironmentId` — ID of the environment
    
</dd>
</dl>

<dl>
<dd>

**guide_id:** `GuideId` — ID of guide
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/flatfile/environments/client.py">update_guide</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a guide
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.environments.update_guide(
    environment_id_="us_env_YOUR_ID",
    guide_id="us_gu_YOUR_ID",
    description="Updated getting started guide",
    title="Data import made easy",
    slug="getting-started",
    environment_id="commons.EnvironmentId",
    metadata={"category": "onboarding"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id_:** `EnvironmentId` — ID of the environment
    
</dd>
</dl>

<dl>
<dd>

**guide_id:** `GuideId` — ID of guide
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**versions:** `typing.Optional[typing.Sequence[GuideVersionResource]]` 
    
</dd>
</dl>

<dl>
<dd>

**blocks:** `typing.Optional[
    typing.Sequence[
        typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
    ]
]` 
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/flatfile/environments/client.py">create_guide</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a guide
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.environments.create_guide(
    environment_id_="us_env_YOUR_ID",
    description="Getting started guide",
    title="Data import made easy",
    slug="getting-started",
    environment_id="commons.EnvironmentId",
    versions=[],
    blocks=[],
    metadata={"category": "onboarding"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id_:** `EnvironmentId` — ID of the environment
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**versions:** `typing.Sequence[GuideVersionResource]` 
    
</dd>
</dl>

<dl>
<dd>

**blocks:** `typing.Sequence[typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]]` 
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/flatfile/environments/client.py">delete_guide</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a guide
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.environments.delete_guide(
    environment_id="us_env_YOUR_ID",
    guide_id="us_gu_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `EnvironmentId` — ID of the environment
    
</dd>
</dl>

<dl>
<dd>

**guide_id:** `GuideId` — ID of guide to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/flatfile/environments/client.py">get_guide_version</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a specified version of a specific guide
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.environments.get_guide_version(
    environment_id="environmentId",
    guide_id="guideId",
    version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `EnvironmentId` — ID of the environment
    
</dd>
</dl>

<dl>
<dd>

**guide_id:** `GuideId` — ID of the guide
    
</dd>
</dl>

<dl>
<dd>

**version:** `int` — Version of the guide
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Events
<details><summary><code>client.events.<a href="src/flatfile/events/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Event topics that the Flatfile Platform emits.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.events.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `typing.Optional[EnvironmentId]` — Filter by environment
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[SpaceId]` — Filter by space
    
</dd>
</dl>

<dl>
<dd>

**domain:** `typing.Optional[str]` — Filter by event domain
    
</dd>
</dl>

<dl>
<dd>

**topic:** `typing.Optional[str]` — Filter by event topic
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[dt.datetime]` — Filter by event timestamp
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return in a page (default 10)
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Based on pageSize, which page of results to return
    
</dd>
</dl>

<dl>
<dd>

**include_acknowledged:** `typing.Optional[bool]` — Include acknowledged events
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/flatfile/events/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile
from flatfile.events import Context

client = Flatfile(
    token="YOUR_TOKEN",
)
client.events.create(
    topic="workbook:updated",
    payload={"recordsAdded": 100},
    domain="workbook",
    context=Context(
        account_id="us_acc_YOUR_ID",
        actor_id="us_key_SOME_KEY",
        environment_id="us_env_YOUR_ID",
        space_id="us_sp_YOUR_ID",
        workbook_id="us_wb_YOUR_ID",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**topic:** `EventTopic` 
    
</dd>
</dl>

<dl>
<dd>

**payload:** `typing.Dict[str, typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**domain:** `Domain` — The domain of the event
    
</dd>
</dl>

<dl>
<dd>

**context:** `Context` — The context of the event
    
</dd>
</dl>

<dl>
<dd>

**deleted_at:** `typing.Optional[dt.datetime]` — Date the event was deleted
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[EventAttributes]` — The attributes of the event
    
</dd>
</dl>

<dl>
<dd>

**callback_url:** `typing.Optional[str]` — The callback url to acknowledge the event
    
</dd>
</dl>

<dl>
<dd>

**data_url:** `typing.Optional[str]` — The url to retrieve the data associated with the event
    
</dd>
</dl>

<dl>
<dd>

**target:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**origin:** `typing.Optional[Origin]` 
    
</dd>
</dl>

<dl>
<dd>

**namespaces:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/flatfile/events/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.events.get(
    event_id="us_evt_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**event_id:** `EventId` — The event id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/flatfile/events/client.py">ack</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.events.ack(
    event_id="eventId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**event_id:** `EventId` — The event id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/flatfile/events/client.py">get_event_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a token which can be used to subscribe to events for this space
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.events.get_event_token()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scope:** `typing.Optional[str]` — The resource ID of the event stream (space or environment id)
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[SpaceId]` — The space ID of the event stream
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Files
<details><summary><code>client.files.<a href="src/flatfile/files/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.files.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of files to return in a page (default 20)
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Based on pageSize, which page of files to return
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[Mode]` — The storage mode of file to fetch, defaults to "import"
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/flatfile/files/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.files.get(
    file_id="us_fl_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/flatfile/files/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.files.delete(
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/flatfile/files/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a file, to change the workbook id for example
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.files.update(
    file_id="us_fl_YOUR_ID",
    name="NewFileName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — ID of file to update
    
</dd>
</dl>

<dl>
<dd>

**workbook_id:** `typing.Optional[WorkbookId]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the file
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[Mode]` — The storage mode of file to update
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ModelFileStatusEnum]` — Status of the file
    
</dd>
</dl>

<dl>
<dd>

**actions:** `typing.Optional[typing.Sequence[Action]]` — The actions attached to the file
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Guests
<details><summary><code>client.guests.<a href="src/flatfile/guests/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all guests
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.guests.list(
    space_id="us_sp_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `SpaceId` — ID of space to return
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Email of guest to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guests.<a href="src/flatfile/guests/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Guests are only there to upload, edit, and download files and perform their tasks in a specific Space.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from flatfile import Flatfile
from flatfile.guests import GuestConfig, GuestSpace, GuestWorkbook

client = Flatfile(
    token="YOUR_TOKEN",
)
client.guests.create(
    request=[
        GuestConfig(
            environment_id="us_env_YOUR_ID",
            email="email@example.com",
            name="Your Name",
            spaces=[
                GuestSpace(
                    id="us_sp_YOUR_ID",
                    workbooks=[
                        GuestWorkbook(
                            id="us_wb_YOUR_ID",
                        )
                    ],
                    last_accessed=datetime.datetime.fromisoformat(
                        "2023-10-30 16:59:45.735000+00:00",
                    ),
                )
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Sequence[GuestConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guests.<a href="src/flatfile/guests/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single guest
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.guests.get(
    guest_id="us_g_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**guest_id:** `GuestId` — ID of guest to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guests.<a href="src/flatfile/guests/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a single guest
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.guests.delete(
    guest_id="us_g_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**guest_id:** `GuestId` — ID of guest to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guests.<a href="src/flatfile/guests/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a single guest, for example to change name or email
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.guests.update(
    guest_id="us_g_YOUR_ID",
    email="updated@example.com",
    name="Your Name Updated",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**guest_id:** `GuestId` — ID of guest to return
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `typing.Optional[EnvironmentId]` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**spaces:** `typing.Optional[typing.Sequence[GuestSpace]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guests.<a href="src/flatfile/guests/client.py">get_guest_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single guest token
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.guests.get_guest_token(
    guest_id="us_g_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**guest_id:** `GuestId` — ID of guest to return
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[SpaceId]` — ID of space to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guests.<a href="src/flatfile/guests/client.py">list_guest_roles</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists roles assigned to a guest.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.guests.list_guest_roles(
    guest_id="guestId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**guest_id:** `GuestId` — The guest id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guests.<a href="src/flatfile/guests/client.py">assign_guest_role</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Assigns a role to a guest.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.guests.assign_guest_role(
    guest_id="guestId",
    role_id="roleId",
    resource_id="resourceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**guest_id:** `GuestId` — The guest id
    
</dd>
</dl>

<dl>
<dd>

**role_id:** `RoleId` 
    
</dd>
</dl>

<dl>
<dd>

**resource_id:** `ResourceIdUnion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guests.<a href="src/flatfile/guests/client.py">delete_guest_role</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a role from a guest.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.guests.delete_guest_role(
    guest_id="guestId",
    actor_role_id="actorRoleId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**guest_id:** `GuestId` — The guest id
    
</dd>
</dl>

<dl>
<dd>

**actor_role_id:** `ActorRoleId` — The actor role id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guests.<a href="src/flatfile/guests/client.py">invite</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Guests can be created as a named guest on the Space or there’s a global link that will let anonymous guests into the space.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile
from flatfile.guests import Invite

client = Flatfile(
    token="YOUR_TOKEN",
)
client.guests.invite(
    request=[
        Invite(
            guest_id="us_g_YOUR_ID",
            space_id="us_sp_YOUR_ID",
            from_name="Your Name",
            message="Hello, I would like to invite you to my space.",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Sequence[Invite]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Jobs
<details><summary><code>client.jobs.<a href="src/flatfile/jobs/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.jobs.list(
    environment_id="us_env_YOUR_ID",
    space_id="us_sp_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `typing.Optional[EnvironmentId]` — When provided, only jobs for the given environment will be returned
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[SpaceId]` — When provided, only jobs for the given space will be returned
    
</dd>
</dl>

<dl>
<dd>

**workbook_id:** `typing.Optional[WorkbookId]` — When provided, only jobs for the given workbook will be returned
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `typing.Optional[FileId]` — When provided, only jobs for the given file will be returned
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[JobId]` — When provided, only jobs that are parts of the given job will be returned
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of jobs to return in a page (default 20)
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Based on pageSize, which page of jobs to return
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction - asc (ascending) or desc (descending)
    
</dd>
</dl>

<dl>
<dd>

**exclude_child_jobs:** `typing.Optional[bool]` — When true, only top-level jobs will be returned unless a parentId is specified
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/flatfile/jobs/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.jobs.create(
    type="workbook",
    operation="submitAction",
    source="us_wb_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `JobType` — The type of job
    
</dd>
</dl>

<dl>
<dd>

**operation:** `str` — the type of operation to perform on the data. For example, "export".
    
</dd>
</dl>

<dl>
<dd>

**source:** `JobSource` 
    
</dd>
</dl>

<dl>
<dd>

**destination:** `typing.Optional[JobDestination]` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[JobUpdateConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**trigger:** `typing.Optional[Trigger]` — the type of trigger to use for this job
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[JobStatus]` — the status of the job
    
</dd>
</dl>

<dl>
<dd>

**progress:** `typing.Optional[int]` — the progress of the job. Whole number between 0 and 100
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `typing.Optional[FileId]` 
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[JobMode]` — the mode of the job
    
</dd>
</dl>

<dl>
<dd>

**input:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Input parameters for this job type.
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[JobSubject]` — Subject parameters for this job type.
    
</dd>
</dl>

<dl>
<dd>

**outcome:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Outcome summary of job.
    
</dd>
</dl>

<dl>
<dd>

**info:** `typing.Optional[str]` — Current status of job in text
    
</dd>
</dl>

<dl>
<dd>

**managed:** `typing.Optional[bool]` — Indicates if Flatfile is managing the control flow of this job or if it is being manually tracked.
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `typing.Optional[EnvironmentId]` — The id of the environment this job belongs to
    
</dd>
</dl>

<dl>
<dd>

**part:** `typing.Optional[int]` — The part number of this job
    
</dd>
</dl>

<dl>
<dd>

**part_data:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The data for this part of the job
    
</dd>
</dl>

<dl>
<dd>

**part_execution:** `typing.Optional[JobPartExecution]` — The execution mode for this part of the job
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[JobId]` — The id of the parent job
    
</dd>
</dl>

<dl>
<dd>

**predecessor_ids:** `typing.Optional[typing.Sequence[JobId]]` — The ids of the jobs that must complete before this job can start
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Additional metadata for the job
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/flatfile/jobs/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.jobs.get(
    job_id="us_jb_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `JobId` — The id of the job to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/flatfile/jobs/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile
from flatfile.jobs import EmptyObject

client = Flatfile(
    token="YOUR_TOKEN",
)
client.jobs.update(
    job_id="us_jb_YOUR_ID",
    config=EmptyObject(),
    status="complete",
    progress=100,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `JobId` — The id of the job to patch
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[JobUpdateConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[JobStatus]` — the status of the job
    
</dd>
</dl>

<dl>
<dd>

**progress:** `typing.Optional[int]` — the progress of the job. Whole number between 0 and 100
    
</dd>
</dl>

<dl>
<dd>

**outcome_acknowledged_at:** `typing.Optional[dt.datetime]` — the time that the job's outcome has been acknowledged by a user
    
</dd>
</dl>

<dl>
<dd>

**info:** `typing.Optional[str]` — Current status of job in text
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Additional metadata for the job
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/flatfile/jobs/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.jobs.delete(
    job_id="us_jb_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `JobId` — The id of the job to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/flatfile/jobs/client.py">execute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a job and return the job
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.jobs.execute(
    job_id="us_jb_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` — ID of job to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/flatfile/jobs/client.py">get_execution_plan</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single job's execution plan
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.jobs.get_execution_plan(
    job_id="us_jb_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `JobId` — ID of job to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/flatfile/jobs/client.py">update_execution_plan</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a job's entire execution plan
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile
from flatfile.jobs import DestinationField, Edge, SourceField
from flatfile.property import Property_String

client = Flatfile(
    token="YOUR_TOKEN",
)
client.jobs.update_execution_plan(
    job_id_="us_jb_YOUR_ID",
    field_mapping=[
        Edge(
            source_field=Property_String(
                key="firstName",
            ),
            destination_field=Property_String(
                key="firstName",
                label="First Name",
            ),
        ),
        Edge(
            source_field=Property_String(
                key="lastName",
            ),
            destination_field=Property_String(
                key="lastName",
                label="Last Name",
            ),
        ),
    ],
    unmapped_source_fields=[
        SourceField(
            source_field=Property_String(
                key="email",
            ),
        )
    ],
    unmapped_destination_fields=[
        DestinationField(
            destination_field=Property_String(
                key="email",
                label="Email",
            ),
        )
    ],
    file_id="us_fl_YOUR_ID",
    job_id="us_jb_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id_:** `JobId` — ID of job to return
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `FileId` 
    
</dd>
</dl>

<dl>
<dd>

**job_id:** `JobId` 
    
</dd>
</dl>

<dl>
<dd>

**field_mapping:** `typing.Sequence[Edge]` 
    
</dd>
</dl>

<dl>
<dd>

**unmapped_source_fields:** `typing.Sequence[SourceField]` 
    
</dd>
</dl>

<dl>
<dd>

**unmapped_destination_fields:** `typing.Sequence[DestinationField]` 
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/flatfile/jobs/client.py">update_execution_plan_fields</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update one or more individual fields on a job's execution plan
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.jobs.update_execution_plan_fields(
    job_id_="jobId",
    file_id="fileId",
    job_id="jobId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id_:** `str` — ID of job to return
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `FileId` 
    
</dd>
</dl>

<dl>
<dd>

**job_id:** `JobId` 
    
</dd>
</dl>

<dl>
<dd>

**field_mapping:** `typing.Optional[typing.Sequence[Edge]]` 
    
</dd>
</dl>

<dl>
<dd>

**unmapped_source_fields:** `typing.Optional[typing.Sequence[SourceField]]` 
    
</dd>
</dl>

<dl>
<dd>

**unmapped_destination_fields:** `typing.Optional[typing.Sequence[DestinationField]]` 
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/flatfile/jobs/client.py">ack</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Acknowledge a job and return the job
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from flatfile import Flatfile
from flatfile.jobs import JobAckDetails

client = Flatfile(
    token="YOUR_TOKEN",
)
client.jobs.ack(
    job_id="us_jb_YOUR_ID",
    request=JobAckDetails(
        info="Acknowledged by user",
        progress=100,
        estimated_completion_at=datetime.datetime.fromisoformat(
            "2023-10-30 20:04:32.074000+00:00",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `JobId` — ID of job to return
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[JobAckDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/flatfile/jobs/client.py">ack_outcome</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Acknowledge a job outcome and return the job
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.jobs.ack_outcome(
    job_id="us_jb_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `JobId` — ID of job to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/flatfile/jobs/client.py">complete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Complete a job and return the job
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile
from flatfile.jobs import JobCompleteDetails, JobOutcome, JobOutcomeNext_Id

client = Flatfile(
    token="YOUR_TOKEN",
)
client.jobs.complete(
    job_id="us_jb_YOUR_ID",
    request=JobCompleteDetails(
        outcome=JobOutcome(
            acknowledge=True,
            button_text="Acknowledge",
            next=JobOutcomeNext_Id(
                id="us_jb_YOUR_ID",
            ),
            heading="Success",
            message="Job was successful",
        ),
        info="Job is Complete",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `JobId` — ID of job to return
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[JobCompleteDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/flatfile/jobs/client.py">fail</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fail a job and return the job
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile
from flatfile.jobs import JobCompleteDetails, JobOutcome, JobOutcomeNext_Id

client = Flatfile(
    token="YOUR_TOKEN",
)
client.jobs.fail(
    job_id="us_jb_YOUR_ID",
    request=JobCompleteDetails(
        outcome=JobOutcome(
            acknowledge=True,
            button_text="Acknowledge",
            next=JobOutcomeNext_Id(
                id="us_jb_YOUR_ID",
            ),
            heading="Failed",
            message="Job failed",
        ),
        info="Job was failed",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `JobId` — ID of job to return
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[JobCompleteDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/flatfile/jobs/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel a job and return the job
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile
from flatfile.jobs import JobCancelDetails

client = Flatfile(
    token="YOUR_TOKEN",
)
client.jobs.cancel(
    job_id="us_jb_YOUR_ID",
    request=JobCancelDetails(
        info="Job was canceled",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `JobId` — ID of job to return
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[JobCancelDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/flatfile/jobs/client.py">retry</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retry a failt job and return the job
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.jobs.retry(
    job_id="jobId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `JobId` — ID of job to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/flatfile/jobs/client.py">preview_mutation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Preview the results of a mutation
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.jobs.preview_mutation(
    sheet_id="sheetId",
    mutate_record="mutateRecord",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sheet_id:** `SheetId` 
    
</dd>
</dl>

<dl>
<dd>

**mutate_record:** `str` — A JavaScript function that will be run on each record in the sheet, it should return a mutated record.
    
</dd>
</dl>

<dl>
<dd>

**mutation_id:** `typing.Optional[str]` — If the mutation was generated through some sort of id-ed process, this links this job and that process.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_label:** `typing.Optional[str]` — If specified, a snapshot will be generated with this label
    
</dd>
</dl>

<dl>
<dd>

**snapshot_id:** `typing.Optional[str]` — The generated snapshotId will be stored here
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[Filter]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_field:** `typing.Optional[FilterField]` 
    
</dd>
</dl>

<dl>
<dd>

**search_value:** `typing.Optional[SearchValue]` 
    
</dd>
</dl>

<dl>
<dd>

**search_field:** `typing.Optional[SearchField]` 
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Sequence[RecordId]]` — The Record Ids param (ids) is a list of record ids that can be passed to several record endpoints allowing the user to identify specific records to INCLUDE in the query, or specific records to EXCLUDE, depending on whether or not filters are being applied. When passing a query param that filters the record dataset, such as 'searchValue', or a 'filter' of 'valid' | 'error' | 'all', the 'ids' param will EXCLUDE those records from the filtered results. For basic queries that do not filter the dataset, passing record ids in the 'ids' param will limit the dataset to INCLUDE just those specific records
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/flatfile/jobs/client.py">split</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Split a job and return the job
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.jobs.split(
    job_id="us_jb_YOUR_ID",
    parts=[{}],
    run_in_parallel=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `JobId` — ID of job to return
    
</dd>
</dl>

<dl>
<dd>

**parts:** `JobParts` 
    
</dd>
</dl>

<dl>
<dd>

**run_in_parallel:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Mapping
<details><summary><code>client.mapping.<a href="src/flatfile/mapping/client.py">create_mapping_program</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a list of mapping rules based on two provided schemas
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile
from flatfile.property import Property_String
from flatfile.sheets import SheetConfig

client = Flatfile(
    token="YOUR_TOKEN",
)
client.mapping.create_mapping_program(
    source=SheetConfig(
        name="name",
        fields=[Property_String(), Property_String()],
    ),
    destination=SheetConfig(
        name="name",
        fields=[Property_String(), Property_String()],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source:** `SheetConfig` — Source schema
    
</dd>
</dl>

<dl>
<dd>

**destination:** `SheetConfig` — Destination schema
    
</dd>
</dl>

<dl>
<dd>

**family_id:** `typing.Optional[FamilyId]` — ID of the family to add the program to
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `typing.Optional[str]` — Namespace of the program
    
</dd>
</dl>

<dl>
<dd>

**save:** `typing.Optional[bool]` — Whether to save the program for editing later. Defaults to false. If true, the response will contain an ID and access token.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mapping.<a href="src/flatfile/mapping/client.py">delete_all_history_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes all history for the authenticated user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.mapping.delete_all_history_for_user()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `typing.Optional[EnvironmentId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mapping.<a href="src/flatfile/mapping/client.py">list_mapping_programs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all mapping programs
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.mapping.list_mapping_programs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of programs to return in a page (default 10)
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Based on pageSize, which page of records to return
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[UserId]` — Filter by creator
    
</dd>
</dl>

<dl>
<dd>

**created_after:** `typing.Optional[dt.datetime]` — Filter by creation time
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[dt.datetime]` — Filter by creation time
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `typing.Optional[EnvironmentId]` — The ID of the environment
    
</dd>
</dl>

<dl>
<dd>

**family_id:** `typing.Optional[FamilyId]` — Filter by family
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `typing.Optional[str]` — Filter by namespace
    
</dd>
</dl>

<dl>
<dd>

**source_keys:** `typing.Optional[str]` — Filter by source keys
    
</dd>
</dl>

<dl>
<dd>

**destination_keys:** `typing.Optional[str]` — Filter by destination keys
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mapping.<a href="src/flatfile/mapping/client.py">get_mapping_program</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a mapping program
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.mapping.get_mapping_program(
    program_id="programId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `ProgramId` — ID of the program
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mapping.<a href="src/flatfile/mapping/client.py">update_mapping_program</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a mapping program
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile
from flatfile.property import Property_String
from flatfile.sheets import SheetConfig

client = Flatfile(
    token="YOUR_TOKEN",
)
client.mapping.update_mapping_program(
    program_id="programId",
    source=SheetConfig(
        name="name",
        fields=[Property_String(), Property_String()],
    ),
    destination=SheetConfig(
        name="name",
        fields=[Property_String(), Property_String()],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `ProgramId` — ID of the program
    
</dd>
</dl>

<dl>
<dd>

**source:** `SheetConfig` — Source schema
    
</dd>
</dl>

<dl>
<dd>

**destination:** `SheetConfig` — Destination schema
    
</dd>
</dl>

<dl>
<dd>

**family_id:** `typing.Optional[FamilyId]` — ID of the family to add the program to
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `typing.Optional[str]` — Namespace of the program
    
</dd>
</dl>

<dl>
<dd>

**save:** `typing.Optional[bool]` — Whether to save the program for editing later. Defaults to false. If true, the response will contain an ID and access token.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mapping.<a href="src/flatfile/mapping/client.py">delete_mapping_program</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a mapping program
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.mapping.delete_mapping_program(
    program_id="programId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `ProgramId` — ID of the program
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mapping.<a href="src/flatfile/mapping/client.py">create_rules</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add mapping rules to a program
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile
from flatfile.mapping import MappingRuleConfig

client = Flatfile(
    token="YOUR_TOKEN",
)
client.mapping.create_rules(
    program_id="programId",
    request=[
        MappingRuleConfig(
            name="name",
            type="type",
        ),
        MappingRuleConfig(
            name="name",
            type="type",
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `ProgramId` — ID of the program
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateMappingRulesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mapping.<a href="src/flatfile/mapping/client.py">delete_multiple_rules</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes multiple mapping rules from a program
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.mapping.delete_multiple_rules(
    program_id="programId",
    rule_ids=["ruleIds", "ruleIds"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `ProgramId` — ID of the program
    
</dd>
</dl>

<dl>
<dd>

**rule_ids:** `typing.Sequence[MappingId]` — Array of rule IDs to be deleted
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mapping.<a href="src/flatfile/mapping/client.py">list_rules</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all mapping rules in a program
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.mapping.list_rules(
    program_id="us_mp_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `ProgramId` — ID of the program
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mapping.<a href="src/flatfile/mapping/client.py">get_rule</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a mapping rule from a program
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.mapping.get_rule(
    program_id="us_mp_YOUR_ID",
    mapping_id="us_mr_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `ProgramId` — ID of the program
    
</dd>
</dl>

<dl>
<dd>

**mapping_id:** `MappingId` — ID of mapping rule
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mapping.<a href="src/flatfile/mapping/client.py">update_rule</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a mapping rule in a program
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.mapping.update_rule(
    program_id="us_mp_YOUR_ID",
    mapping_id="us_mr_YOUR_ID",
    name="Assign mapping rule",
    type="assign",
    config={},
    metadata={},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `ProgramId` — ID of the program
    
</dd>
</dl>

<dl>
<dd>

**mapping_id:** `MappingId` — ID of mapping rule
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the mapping rule
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**accepted_at:** `typing.Optional[dt.datetime]` — Time the mapping rule was last updated
    
</dd>
</dl>

<dl>
<dd>

**accepted_by:** `typing.Optional[UserId]` — User ID of the contributor of the mapping rule
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Optional[typing.Any]]` — Metadata of the mapping rule
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mapping.<a href="src/flatfile/mapping/client.py">update_rules</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a list of mapping rules in a program
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from flatfile import Flatfile
from flatfile.mapping import MappingRule

client = Flatfile(
    token="YOUR_TOKEN",
)
client.mapping.update_rules(
    program_id="programId",
    request=[
        MappingRule(
            id="id",
            created_at=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            updated_at=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        ),
        MappingRule(
            id="id",
            created_at=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            updated_at=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `ProgramId` — ID of the program
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateMappingRulesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mapping.<a href="src/flatfile/mapping/client.py">delete_rule</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a mapping rule from a program
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.mapping.delete_rule(
    program_id="us_mp_YOUR_ID",
    mapping_id="us_mr_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `ProgramId` — ID of the program
    
</dd>
</dl>

<dl>
<dd>

**mapping_id:** `MappingId` — ID of mapping rule
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Records
<details><summary><code>client.records.<a href="src/flatfile/records/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns records from a sheet in a workbook
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.records.get(
    sheet_id="us_sh_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sheet_id:** `SheetId` — ID of sheet
    
</dd>
</dl>

<dl>
<dd>

**version_id:** `typing.Optional[VersionId]` — Deprecated, use `commitId` instead.
    
</dd>
</dl>

<dl>
<dd>

**commit_id:** `typing.Optional[CommitId]` 
    
</dd>
</dl>

<dl>
<dd>

**since_version_id:** `typing.Optional[VersionId]` — Deprecated, use `sinceCommitId` instead.
    
</dd>
</dl>

<dl>
<dd>

**since_commit_id:** `typing.Optional[CommitId]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[SortField]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[Filter]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_field:** `typing.Optional[FilterField]` — Name of field by which to filter records
    
</dd>
</dl>

<dl>
<dd>

**search_value:** `typing.Optional[SearchValue]` 
    
</dd>
</dl>

<dl>
<dd>

**search_field:** `typing.Optional[SearchField]` 
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[RecordId, typing.Sequence[RecordId]]]` — The Record Ids param (ids) is a list of record ids that can be passed to several record endpoints allowing the user to identify specific records to INCLUDE in the query, or specific records to EXCLUDE, depending on whether or not filters are being applied. When passing a query param that filters the record dataset, such as 'searchValue', or a 'filter' of 'valid' | 'error' | 'all', the 'ids' param will EXCLUDE those records from the filtered results. For basic queries that do not filter the dataset, passing record ids in the 'ids' param will limit the dataset to INCLUDE just those specific records. Maximum of 100 allowed.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of records to return in a page (default 10,000)
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Based on pageSize, which page of records to return (Note - numbers start at 1)
    
</dd>
</dl>

<dl>
<dd>

**include_counts:** `typing.Optional[bool]` — **DEPRECATED** Use GET /sheets/:sheetId/counts
    
</dd>
</dl>

<dl>
<dd>

**include_length:** `typing.Optional[bool]` — The length of the record result set, returned as counts.total
    
</dd>
</dl>

<dl>
<dd>

**include_links:** `typing.Optional[bool]` — If true, linked records will be included in the results. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**include_messages:** `typing.Optional[bool]` — Include error messages, defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of field keys to include in the response. If not provided, all fields will be included.
    
</dd>
</dl>

<dl>
<dd>

**for_:** `typing.Optional[EventId]` — if "for" is provided, the query parameters will be pulled from the event payload
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — An FFQL query used to filter the result set
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.records.<a href="src/flatfile/records/client.py">indices</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns indices of records from a sheet in a workbook
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.records.indices(
    sheet_id="us_sh_YOUR_ID",
    ids="list<$commons.RecordId.Example0, $commons.RecordId.Example1>",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sheet_id:** `SheetId` — ID of sheet
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Union[RecordId, typing.Sequence[RecordId]]` — List of record IDs to include in the query. Limit 100.
    
</dd>
</dl>

<dl>
<dd>

**commit_id:** `typing.Optional[CommitId]` 
    
</dd>
</dl>

<dl>
<dd>

**since_commit_id:** `typing.Optional[CommitId]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[SortField]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[Filter]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_field:** `typing.Optional[FilterField]` — Name of field by which to filter records
    
</dd>
</dl>

<dl>
<dd>

**search_value:** `typing.Optional[SearchValue]` 
    
</dd>
</dl>

<dl>
<dd>

**search_field:** `typing.Optional[SearchField]` 
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — An FFQL query used to filter the result set
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.records.<a href="src/flatfile/records/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates existing records in a workbook sheet
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile
from flatfile.records import CellValue, Record, RecordConfig

client = Flatfile(
    token="YOUR_TOKEN",
)
client.records.update(
    sheet_id="us_sh_YOUR_ID",
    request=[
        Record(
            id="us_rc_YOUR_ID",
            version_id="us_vr_YOUR_ID",
            commit_id="us_vr_YOUR_ID",
            values={
                "firstName": CellValue(
                    value="John",
                    messages=[],
                    valid=True,
                ),
                "lastName": CellValue(
                    value="Smith",
                    messages=[],
                    valid=True,
                ),
                "email": CellValue(
                    value="john.smith@example.com",
                    messages=[],
                    valid=True,
                ),
            },
            valid=True,
            metadata={},
            config=RecordConfig(),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sheet_id:** `SheetId` — ID of sheet
    
</dd>
</dl>

<dl>
<dd>

**request:** `Records` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.records.<a href="src/flatfile/records/client.py">insert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds records to a workbook sheet
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile
from flatfile.records import CellValue

client = Flatfile(
    token="YOUR_TOKEN",
)
client.records.insert(
    sheet_id="us_sh_YOUR_ID",
    request=[
        {
            "firstName": CellValue(
                value="John",
                messages=[],
                valid=True,
            ),
            "lastName": CellValue(
                value="Smith",
                messages=[],
                valid=True,
            ),
            "email": CellValue(
                value="john.smith@example.com",
                messages=[],
                valid=True,
            ),
        }
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sheet_id:** `SheetId` — ID of sheet
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Sequence[RecordData]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.records.<a href="src/flatfile/records/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes records from a workbook sheet
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.records.delete(
    sheet_id="us_sh_YOUR_ID",
    ids="us_rc_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sheet_id:** `SheetId` — ID of sheet
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Union[RecordId, typing.Sequence[RecordId]]` — A list of record IDs to delete. Maximum of 100 allowed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.records.<a href="src/flatfile/records/client.py">find_and_replace</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for all values that match the 'find' value (globally or for a specific field via 'fieldKey') and replaces them with the 'replace' value. Wrap 'find' value in double quotes for exact match (""). Returns a commitId for the updated records
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.records.find_and_replace(
    sheet_id="us_sh_YOUR_ID",
    field_key="email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sheet_id:** `SheetId` — ID of sheet
    
</dd>
</dl>

<dl>
<dd>

**field_key:** `str` — A unique key used to identify a field in a sheet
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[Filter]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_field:** `typing.Optional[FilterField]` — Name of field by which to filter records
    
</dd>
</dl>

<dl>
<dd>

**search_value:** `typing.Optional[SearchValue]` 
    
</dd>
</dl>

<dl>
<dd>

**search_field:** `typing.Optional[SearchField]` 
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[RecordId, typing.Sequence[RecordId]]]` — The Record Ids param (ids) is a list of record ids that can be passed to several record endpoints allowing the user to identify specific records to INCLUDE in the query, or specific records to EXCLUDE, depending on whether or not filters are being applied. When passing a query param that filters the record dataset, such as 'searchValue', or a 'filter' of 'valid' | 'error' | 'all', the 'ids' param will EXCLUDE those records from the filtered results. For basic queries that do not filter the dataset, passing record ids in the 'ids' param will limit the dataset to INCLUDE just those specific records
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — An FFQL query used to filter the result set
    
</dd>
</dl>

<dl>
<dd>

**find:** `typing.Optional[CellValueUnion]` — A value to find for a given field in a sheet. For exact matches, wrap the value in double quotes ("Bob")
    
</dd>
</dl>

<dl>
<dd>

**replace:** `typing.Optional[CellValueUnion]` — The value to replace found values with
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Roles
<details><summary><code>client.roles.<a href="src/flatfile/roles/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all roles for an account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.roles.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Secrets
<details><summary><code>client.secrets.<a href="src/flatfile/secrets/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch all secrets for a given environmentId and optionally apply space overrides
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.secrets.list(
    environment_id="us_env_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `typing.Optional[EnvironmentId]` — The Environment of the secret.
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[SpaceId]` — The Space of the secret.
    
</dd>
</dl>

<dl>
<dd>

**actor_id:** `typing.Optional[ActorIdUnion]` — The Actor of the secret.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.secrets.<a href="src/flatfile/secrets/client.py">upsert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Insert or Update a Secret by name for environment or space
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.secrets.upsert(
    name="My Secret",
    value="Sup3r$ecret\\/alue!",
    environment_id="us_env_YOUR_ID",
    space_id="us_sp_YOUR_ID",
    actor_id="us_usr_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `SecretName` — The reference name for a secret.
    
</dd>
</dl>

<dl>
<dd>

**value:** `SecretValue` — The secret value. This is hidden in the UI.
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `typing.Optional[EnvironmentId]` — The Environment of the secret.
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[SpaceId]` — The Space of the secret.
    
</dd>
</dl>

<dl>
<dd>

**actor_id:** `typing.Optional[ActorIdUnion]` — The Actor of the secret.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.secrets.<a href="src/flatfile/secrets/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a specific Secret from the Environment or Space as is the case
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.secrets.delete(
    secret_id="us_sec_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**secret_id:** `SecretId` — The ID of the secret.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sheets
<details><summary><code>client.sheets.<a href="src/flatfile/sheets/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns sheets in a workbook
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.sheets.list(
    workbook_id="us_wb_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workbook_id:** `WorkbookId` — ID of workbook
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sheets.<a href="src/flatfile/sheets/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a sheet in a workbook
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.sheets.get(
    sheet_id="us_sh_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sheet_id:** `SheetId` — ID of sheet
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sheets.<a href="src/flatfile/sheets/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a specific sheet from a workbook
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.sheets.delete(
    sheet_id="us_sh_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sheet_id:** `SheetId` — ID of sheet
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sheets.<a href="src/flatfile/sheets/client.py">validate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Trigger data hooks and validation to run on a sheet
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.sheets.validate(
    sheet_id="us_sh_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sheet_id:** `SheetId` — ID of sheet
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sheets.<a href="src/flatfile/sheets/client.py">get_record_counts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns counts of records from a sheet
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.sheets.get_record_counts(
    sheet_id="us_sh_YOUR_ID",
    version_id="us_vr_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sheet_id:** `SheetId` — ID of sheet
    
</dd>
</dl>

<dl>
<dd>

**version_id:** `typing.Optional[str]` — Returns records that were changed in that version and only those records.
    
</dd>
</dl>

<dl>
<dd>

**since_version_id:** `typing.Optional[VersionId]` — Deprecated, use `sinceCommitId` instead.
    
</dd>
</dl>

<dl>
<dd>

**commit_id:** `typing.Optional[CommitId]` — Returns records that were changed in that version in addition to any records from versions after that version.
    
</dd>
</dl>

<dl>
<dd>

**since_commit_id:** `typing.Optional[CommitId]` — Listing a commit ID here will return all records since the specified commit.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[Filter]` — Options to filter records
    
</dd>
</dl>

<dl>
<dd>

**filter_field:** `typing.Optional[FilterField]` — The field to filter the data on.
    
</dd>
</dl>

<dl>
<dd>

**search_value:** `typing.Optional[SearchValue]` — The value to search for data on.
    
</dd>
</dl>

<dl>
<dd>

**search_field:** `typing.Optional[SearchField]` — The field to search for data on.
    
</dd>
</dl>

<dl>
<dd>

**by_field:** `typing.Optional[bool]` — If true, the counts for each field will also be returned
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — An FFQL query used to filter the result set to be counted
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sheets.<a href="src/flatfile/sheets/client.py">get_sheet_commits</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the commit versions for a sheet
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.sheets.get_sheet_commits(
    sheet_id="us_sh_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sheet_id:** `SheetId` — ID of sheet
    
</dd>
</dl>

<dl>
<dd>

**completed:** `typing.Optional[bool]` — If true, only return commits that have been completed. If false, only return commits that have not been completed. If not provided, return all commits.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sheets.<a href="src/flatfile/sheets/client.py">lock_sheet</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Locks a sheet
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.sheets.lock_sheet(
    sheet_id="us_sh_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sheet_id:** `SheetId` — ID of sheet
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sheets.<a href="src/flatfile/sheets/client.py">unlock_sheet</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a lock from a sheet
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.sheets.unlock_sheet(
    sheet_id="us_sh_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sheet_id:** `SheetId` — ID of sheet
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sheets.<a href="src/flatfile/sheets/client.py">get_cell_values</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns record cell values grouped by all fields in the sheet
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.sheets.get_cell_values(
    sheet_id="us_sh_YOUR_ID",
    distinct=True,
    field_key="firstName",
    sort_field="firstName",
    sort_direction="asc",
    filter="valid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sheet_id:** `SheetId` — ID of sheet
    
</dd>
</dl>

<dl>
<dd>

**distinct:** `Distinct` — Must be set to true
    
</dd>
</dl>

<dl>
<dd>

**field_key:** `typing.Optional[FieldKey]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[SortField]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[Filter]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_field:** `typing.Optional[FilterField]` — Name of field by which to filter records
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[PageSize]` — Number of records to return in a page (default 1000 if pageNumber included)
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[PageNumber]` — Based on pageSize, which page of records to return
    
</dd>
</dl>

<dl>
<dd>

**include_counts:** `typing.Optional[IncludeCounts]` 
    
</dd>
</dl>

<dl>
<dd>

**search_value:** `typing.Optional[SearchValue]` — A value to find for a given field in a sheet. Wrap the value in "" for exact match
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sheets.<a href="src/flatfile/sheets/client.py">update_sheet</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates Sheet
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.sheets.update_sheet(
    sheet_id="us_sh_YOUR_ID",
    name="New Sheet Name",
    metadata={"rowHeaders": [6]},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sheet_id:** `SheetId` — ID of sheet
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the Sheet.
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` — The slug of the Sheet.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Optional[typing.Any]]` — Useful for any contextual metadata regarding the sheet. Store any valid json
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Snapshots
<details><summary><code>client.snapshots.<a href="src/flatfile/snapshots/client.py">create_snapshot</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a snapshot of a sheet
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.snapshots.create_snapshot(
    sheet_id="us_sh_YOUR_ID",
    label="My snapshot",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sheet_id:** `SheetId` — ID of sheet
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — Label for the snapshot
    
</dd>
</dl>

<dl>
<dd>

**thread_id:** `typing.Optional[str]` — ThreadId for the snapshot
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.snapshots.<a href="src/flatfile/snapshots/client.py">list_snapshots</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all snapshots of a sheet
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.snapshots.list_snapshots(
    sheet_id="us_sh_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sheet_id:** `SheetId` — ID of sheet
    
</dd>
</dl>

<dl>
<dd>

**thread_id:** `typing.Optional[str]` — ThreadId to filter snapshots by
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.snapshots.<a href="src/flatfile/snapshots/client.py">get_snapshot</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a snapshot of a sheet
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.snapshots.get_snapshot(
    snapshot_id="us_ss_YOUR_ID",
    include_summary=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**snapshot_id:** `SnapshotId` — ID of snapshot
    
</dd>
</dl>

<dl>
<dd>

**include_summary:** `bool` — Whether to include a summary in the snapshot response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.snapshots.<a href="src/flatfile/snapshots/client.py">delete_snapshot</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a snapshot of a sheet
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.snapshots.delete_snapshot(
    snapshot_id="us_ss_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**snapshot_id:** `SnapshotId` — ID of snapshot
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.snapshots.<a href="src/flatfile/snapshots/client.py">restore_snapshot</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restores a snapshot of a sheet
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile
from flatfile.snapshots import RestoreOptions

client = Flatfile(
    token="YOUR_TOKEN",
)
client.snapshots.restore_snapshot(
    snapshot_id="us_ss_YOUR_ID",
    request=RestoreOptions(
        created=True,
        updated=True,
        deleted=True,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**snapshot_id:** `SnapshotId` — ID of snapshot
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[RestoreOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.snapshots.<a href="src/flatfile/snapshots/client.py">get_snapshot_records</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets records from a snapshot of a sheet
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.snapshots.get_snapshot_records(
    snapshot_id="us_ss_YOUR_ID",
    page_size=10,
    page_number=1,
    change_type="createdSince",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**snapshot_id:** `SnapshotId` — ID of snapshot
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of records to return in a page
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Based on pageSize, which page of records to return
    
</dd>
</dl>

<dl>
<dd>

**change_type:** `typing.Optional[ChangeType]` — Filter records by change type
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Spaces
<details><summary><code>client.spaces.<a href="src/flatfile/spaces/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all spaces for an account or environment
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.spaces.list(
    environment_id="us_env_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `typing.Optional[EnvironmentId]` — The ID of the environment.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of spaces to return in a page (default 10)
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Based on pageSize, which page of records to return
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search query for spaces
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `typing.Optional[str]` — Search by namespace
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` — Flag to include archived spaces
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetSpacesSortField]` — Field to sort spaces by; requires `sortDirection` if provided.
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Direction of sorting; requires `sortField` if provided.
    
</dd>
</dl>

<dl>
<dd>

**is_collaborative:** `typing.Optional[bool]` — Flag for collaborative (project) spaces
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `typing.Optional[AppId]` — Filter by appId
    
</dd>
</dl>

<dl>
<dd>

**is_app_template:** `typing.Optional[bool]` — Flag for app templates
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.spaces.<a href="src/flatfile/spaces/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new space based on an existing Space Config
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.spaces.create(
    name="My First Workbook",
    display_order=1,
    environment_id="us_env_YOUR_ID",
    primary_workbook_id="us_wb_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the space
    
</dd>
</dl>

<dl>
<dd>

**display_order:** `typing.Optional[int]` — The display order
    
</dd>
</dl>

<dl>
<dd>

**guest_authentication:** `typing.Optional[typing.Sequence[GuestAuthenticationEnum]]` 
    
</dd>
</dl>

<dl>
<dd>

**space_config_id:** `typing.Optional[SpaceConfigId]` 
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `typing.Optional[EnvironmentId]` 
    
</dd>
</dl>

<dl>
<dd>

**primary_workbook_id:** `typing.Optional[WorkbookId]` — The ID of the primary workbook for the space. This should not be included in create space requests.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Optional[typing.Any]]` — Metadata for the space
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[SpaceSettings]` — The Space settings.
    
</dd>
</dl>

<dl>
<dd>

**actions:** `typing.Optional[typing.Sequence[Action]]` 
    
</dd>
</dl>

<dl>
<dd>

**access:** `typing.Optional[typing.Sequence[SpaceAccess]]` 
    
</dd>
</dl>

<dl>
<dd>

**auto_configure:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**translations_path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**language_override:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**archived_at:** `typing.Optional[dt.datetime]` — Date when space was archived
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `typing.Optional[AppId]` — The ID of the App that space is associated with
    
</dd>
</dl>

<dl>
<dd>

**is_app_template:** `typing.Optional[bool]` — Whether the space is an app template. Only one space per app can be an app template.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.spaces.<a href="src/flatfile/spaces/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single space
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.spaces.get(
    space_id="us_sp_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `SpaceId` — ID of space to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.spaces.<a href="src/flatfile/spaces/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a space
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.spaces.delete(
    space_id="us_sp_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `SpaceId` — ID of space to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.spaces.<a href="src/flatfile/spaces/client.py">bulk_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete multiple spaces by id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.spaces.bulk_delete(
    space_ids="us_sp_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_ids:** `typing.Union[SpaceId, typing.Sequence[SpaceId]]` — List of ids for the spaces to be deleted
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.spaces.<a href="src/flatfile/spaces/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a space, to change the name for example
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.spaces.update(
    space_id="us_sp_YOUR_ID",
    name="My Updated Worbook",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `SpaceId` — ID of space to update
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the space
    
</dd>
</dl>

<dl>
<dd>

**display_order:** `typing.Optional[int]` — The display order
    
</dd>
</dl>

<dl>
<dd>

**guest_authentication:** `typing.Optional[typing.Sequence[GuestAuthenticationEnum]]` 
    
</dd>
</dl>

<dl>
<dd>

**space_config_id:** `typing.Optional[SpaceConfigId]` 
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `typing.Optional[EnvironmentId]` 
    
</dd>
</dl>

<dl>
<dd>

**primary_workbook_id:** `typing.Optional[WorkbookId]` — The ID of the primary workbook for the space. This should not be included in create space requests.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Optional[typing.Any]]` — Metadata for the space
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[SpaceSettings]` — The Space settings.
    
</dd>
</dl>

<dl>
<dd>

**actions:** `typing.Optional[typing.Sequence[Action]]` 
    
</dd>
</dl>

<dl>
<dd>

**access:** `typing.Optional[typing.Sequence[SpaceAccess]]` 
    
</dd>
</dl>

<dl>
<dd>

**auto_configure:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**translations_path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**language_override:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**archived_at:** `typing.Optional[dt.datetime]` — Date when space was archived
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `typing.Optional[AppId]` — The ID of the App that space is associated with
    
</dd>
</dl>

<dl>
<dd>

**is_app_template:** `typing.Optional[bool]` — Whether the space is an app template. Only one space per app can be an app template.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.spaces.<a href="src/flatfile/spaces/client.py">archive_space</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets archivedAt timestamp on a space
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.spaces.archive_space(
    space_id="us_sp_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `SpaceId` — ID of space to archive
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.spaces.<a href="src/flatfile/spaces/client.py">unarchive_space</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets archivedAt timestamp on a space to null
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.spaces.unarchive_space(
    space_id="us_sp_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `SpaceId` — ID of space to unarchive
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.spaces.<a href="src/flatfile/spaces/client.py">create_guidance</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new guidance
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile
from flatfile.spaces import GuidanceOptions

client = Flatfile(
    token="YOUR_TOKEN",
)
client.spaces.create_guidance(
    space_id="spaceId",
    guide_slug="guideSlug",
    options=GuidanceOptions(
        target="target",
        trigger="first",
        type="sidebar",
        role="admin",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `SpaceId` — ID of the space
    
</dd>
</dl>

<dl>
<dd>

**guide_slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `GuidanceOptions` — Options for the guidance
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.spaces.<a href="src/flatfile/spaces/client.py">list_guidance</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists guidances
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.spaces.list_guidance(
    space_id="spaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `SpaceId` — ID of the space
    
</dd>
</dl>

<dl>
<dd>

**guide:** `typing.Optional[str]` — Include the guide with the guidance
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.spaces.<a href="src/flatfile/spaces/client.py">get_guidance</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a guidance by its id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.spaces.get_guidance(
    space_id="spaceId",
    guidance_id="guidanceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `SpaceId` — ID of the space
    
</dd>
</dl>

<dl>
<dd>

**guidance_id:** `GuidanceId` — ID of the guidance
    
</dd>
</dl>

<dl>
<dd>

**guide:** `typing.Optional[str]` — Include the guide with the guidance
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.spaces.<a href="src/flatfile/spaces/client.py">update_guidance</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a guidance with the given id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile
from flatfile.spaces import GuidanceOptions

client = Flatfile(
    token="YOUR_TOKEN",
)
client.spaces.update_guidance(
    space_id="spaceId",
    guidance_id="guidanceId",
    options=GuidanceOptions(
        target="target",
        trigger="first",
        type="sidebar",
        role="admin",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `SpaceId` — ID of the space
    
</dd>
</dl>

<dl>
<dd>

**guidance_id:** `GuidanceId` — ID of the guidance
    
</dd>
</dl>

<dl>
<dd>

**options:** `GuidanceOptions` — Options for the guidance
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.spaces.<a href="src/flatfile/spaces/client.py">delete_guidance</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a guidance by its id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.spaces.delete_guidance(
    space_id="spaceId",
    guidance_id="guidanceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `SpaceId` — ID of the space
    
</dd>
</dl>

<dl>
<dd>

**guidance_id:** `GuidanceId` — ID of the guidance
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users
<details><summary><code>client.users.<a href="src/flatfile/users/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of users
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.users.list(
    email="john.smith@example.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `typing.Optional[str]` — Email of guest to return
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — String to search for users by name and email
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[ListUsersSortField]` — Field to sort users by
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Direction of sorting
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of users to return in a page (default 20)
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Based on pageSize, which page of users to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/flatfile/users/client.py">create_and_invite</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates and invites a new user to your account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile
from flatfile.roles import AssignActorRoleRequest

client = Flatfile(
    token="YOUR_TOKEN",
)
client.users.create_and_invite(
    email="john.smith@example.com",
    name="John Smith",
    actor_roles=[
        AssignActorRoleRequest(
            role_id="us_rol_YOUR_ID",
            resource_id="us_acc_YOUR_ID",
        ),
        AssignActorRoleRequest(
            role_id="us_rol_YOUR_ID",
            resource_id="us_env_YOUR_ID",
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**actor_roles:** `typing.Sequence[AssignActorRoleRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/flatfile/users/client.py">resend_invite</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resends an invite to a user for your account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.users.resend_invite(
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `UserId` — The user id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/flatfile/users/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.users.update(
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `UserId` — The user id
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**dashboard:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/flatfile/users/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.users.get(
    user_id="us_usr_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `UserId` — The user id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/flatfile/users/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.users.delete(
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `UserId` — The user id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/flatfile/users/client.py">list_user_roles</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists roles assigned to a user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.users.list_user_roles(
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `UserId` — The user id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/flatfile/users/client.py">assign_user_role</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Assigns a role to a user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.users.assign_user_role(
    user_id="userId",
    role_id="roleId",
    resource_id="resourceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `UserId` — The user id
    
</dd>
</dl>

<dl>
<dd>

**role_id:** `RoleId` 
    
</dd>
</dl>

<dl>
<dd>

**resource_id:** `ResourceIdUnion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/flatfile/users/client.py">delete_user_role</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a role from a user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.users.delete_user_role(
    user_id="userId",
    actor_role_id="actorRoleId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `UserId` — The user id
    
</dd>
</dl>

<dl>
<dd>

**actor_role_id:** `ActorRoleId` — The actor role id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Versions
<details><summary><code>client.versions.<a href="src/flatfile/versions/client.py">create_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.versions.create_id(
    sheet_id="us_sh_YOUR_ID",
    parent_version_id="us_vr_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sheet_id:** `typing.Optional[SheetId]` — The ID of the Sheet.
    
</dd>
</dl>

<dl>
<dd>

**parent_version_id:** `typing.Optional[VersionId]` — Deprecated, creating or updating a group of records together will automatically generate a commitId to group those record changes together.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Views
<details><summary><code>client.views.<a href="src/flatfile/views/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all views for the sheet
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.views.list(
    sheet_id="us_sh_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sheet_id:** `SheetId` — The associated sheet ID of the view.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of prompts to return in a page (default 10)
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Based on pageSize, which page of prompts to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.views.<a href="src/flatfile/views/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new view to the space
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile
from flatfile.views import ViewConfig

client = Flatfile(
    token="YOUR_TOKEN",
)
client.views.create(
    sheet_id="us_sh_YOUR_ID",
    name="My View",
    config=ViewConfig(
        filter="error",
        filter_field="email",
        q="firstname like %John%",
        sort_field="email",
        sort_direction="asc",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sheet_id:** `SheetId` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `ViewConfig` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.views.<a href="src/flatfile/views/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single view
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.views.get(
    view_id="us_vi_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**view_id:** `ViewId` — ID of view to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.views.<a href="src/flatfile/views/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a single view
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile
from flatfile.views import ViewConfig

client = Flatfile(
    token="YOUR_TOKEN",
)
client.views.update(
    view_id="us_vi_YOUR_ID",
    name="My View",
    config=ViewConfig(
        filter="error",
        filter_field="email",
        q="firstname like %John%",
        sort_field="email",
        sort_direction="asc",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**view_id:** `ViewId` — ID of view to update
    
</dd>
</dl>

<dl>
<dd>

**config:** `ViewConfig` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.views.<a href="src/flatfile/views/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a single view
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.views.delete(
    view_id="us_vi_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**view_id:** `ViewId` — ID of view to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Workbooks
<details><summary><code>client.workbooks.<a href="src/flatfile/workbooks/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all workbooks matching a filter for an account or space
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.workbooks.list(
    space_id="us_sp_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**space_id:** `typing.Optional[SpaceId]` — The associated Space ID of the Workbook.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter by name. Precede with - to negate the filter
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `typing.Optional[str]` — Filter by namespace. Precede with - to negate the filter
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — Filter by label. Precede with - to negate the filter
    
</dd>
</dl>

<dl>
<dd>

**treatment:** `typing.Optional[str]` — Filter by treatment.
    
</dd>
</dl>

<dl>
<dd>

**include_sheets:** `typing.Optional[bool]` — Include sheets for the workbook (default true)
    
</dd>
</dl>

<dl>
<dd>

**include_counts:** `typing.Optional[bool]` — Include counts for the workbook. **DEPRECATED** Counts will return 0s. Use GET /sheets/:sheetId/counts
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workbooks.<a href="src/flatfile/workbooks/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a workbook and adds it to a space
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile
from flatfile.commons import Action
from flatfile.property import Property_String
from flatfile.sheets import SheetConfig
from flatfile.workbooks import WorkbookConfigSettings

client = Flatfile(
    token="YOUR_TOKEN",
)
client.workbooks.create(
    name="My First Workbook",
    sheets=[
        SheetConfig(
            name="Contacts",
            slug="contacts",
            fields=[
                Property_String(
                    key="firstName",
                    label="First Name",
                ),
                Property_String(
                    key="lastName",
                    label="Last Name",
                ),
                Property_String(
                    key="email",
                    label="Email",
                ),
            ],
            mapping_confidence_threshold=0.5,
        )
    ],
    labels=["simple-demo"],
    actions=[
        Action(
            operation="submitAction",
            mode="foreground",
            label="Submit",
            description="Submit data to webhook.site",
            primary=True,
        )
    ],
    settings=WorkbookConfigSettings(
        track_changes=True,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the Workbook.
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.Sequence[str]]` — An optional list of labels for the Workbook.
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[SpaceId]` — Space to associate with the Workbook.
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `typing.Optional[EnvironmentId]` — Environment to associate with the Workbook
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `typing.Optional[str]` — Optional namespace to apply to the Workbook.
    
</dd>
</dl>

<dl>
<dd>

**sheets:** `typing.Optional[typing.Sequence[SheetConfig]]` — Sheets to create on the Workbook.
    
</dd>
</dl>

<dl>
<dd>

**actions:** `typing.Optional[typing.Sequence[Action]]` — Actions to create on the Workbook.
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[WorkbookConfigSettings]` — The Workbook settings.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Optional[typing.Any]]` — Metadata for the workbook
    
</dd>
</dl>

<dl>
<dd>

**treatments:** `typing.Optional[typing.Sequence[WorkbookTreatments]]` — Treatments for the workbook
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workbooks.<a href="src/flatfile/workbooks/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single workbook
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.workbooks.get(
    workbook_id="us_wb_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workbook_id:** `WorkbookId` — ID of workbook to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workbooks.<a href="src/flatfile/workbooks/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a workbook and all of its record data permanently
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.workbooks.delete(
    workbook_id="us_wb_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workbook_id:** `WorkbookId` — ID of workbook to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workbooks.<a href="src/flatfile/workbooks/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a workbook
<Note>
  Adding a sheet to a workbook does not require the config object to be provided, however updating an existing sheet does.
</Note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile
from flatfile.commons import Action

client = Flatfile(
    token="YOUR_TOKEN",
)
client.workbooks.update(
    workbook_id="us_wb_YOUR_ID",
    name="My Updated Workbook",
    labels=["my-new-label"],
    actions=[
        Action(
            operation="submitAction",
            mode="foreground",
            label="Submit Changes",
            description="Submit data to webhook.site",
            primary=True,
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workbook_id:** `WorkbookId` — ID of workbook to update
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the Workbook.
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.Sequence[str]]` — An optional list of labels for the Workbook.
    
</dd>
</dl>

<dl>
<dd>

**space_id:** `typing.Optional[SpaceId]` — The Space Id associated with the Workbook.
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `typing.Optional[EnvironmentId]` — The Environment Id associated with the Workbook.
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `typing.Optional[str]` — The namespace of the Workbook.
    
</dd>
</dl>

<dl>
<dd>

**sheets:** `typing.Optional[typing.Sequence[SheetConfigOrUpdate]]` — Describes shape of data as well as behavior
    
</dd>
</dl>

<dl>
<dd>

**actions:** `typing.Optional[typing.Sequence[Action]]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Optional[typing.Any]]` — Metadata for the workbook
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[WorkbookConfigSettings]` — The Workbook settings.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workbooks.<a href="src/flatfile/workbooks/client.py">get_workbook_commits</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the commits for a workbook
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flatfile import Flatfile

client = Flatfile(
    token="YOUR_TOKEN",
)
client.workbooks.get_workbook_commits(
    workbook_id="us_wb_YOUR_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workbook_id:** `WorkbookId` — ID of workbook
    
</dd>
</dl>

<dl>
<dd>

**completed:** `typing.Optional[bool]` — If true, only return commits that have been completed. If false, only return commits that have not been completed. If not provided, return all commits.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

