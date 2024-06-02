# AutoForks

这是一个自动化工具，用于定期从 GitHub 中 fork 感兴趣的仓库。它使用 GitHub Actions 来每隔几小时自动执行 fork 操作，并记录操作结果。

## 功能

- 定时检查指定的 GitHub 仓库。
- 自动 fork 新的仓库。
- 记录每次 fork 操作的详细日志。

## 使用前的配置

在开始使用这个自动化工具之前，您需要进行以下几步配置：

1. **Fork 或 Clone 这个仓库**

   - 通过 GitHub 上的 Fork 功能将这个仓库复制到您的账号下，或者 Clone 到您的本地环境。

2. **创建 GitHub 个人访问令牌**

   - 访问 [GitHub Tokens Settings](https://github.com/settings/tokens)。
   - 点击“Generate new token”，选择适当的权限，至少包括对仓库的读写权限。
   - 生成后，请复制并保存好这个令牌，它不会再次显示。

3. **配置 GitHub Secrets**

   - 进入您的仓库设置，点击“Secrets”然后选择“Actions”。
   - 点击“New repository secret”，创建以下两个密钥：
     - `GITHUB_USERNAME`：您的 GitHub 用户名。
     - `GITHUB_TOKEN`：您在上一步中生成的 GitHub 访问令牌。

4. **配置工作流**
   - 工作流文件位于`.github/workflows/auto_fork.yml`。
   - 根据需要调整工作流文件中的 cron 设置，以更改执行频率。

## 使用方法

一旦完成上述配置，工具将自动按照配置的时间间隔运行。您可以在 GitHub Actions 的日志中查看每次运行的结果。

## 贡献

欢迎对这个工具进行任何形式的贡献，无论是功能增强、错误修复还是文档改进。请通过 Pull Requests 或 Issues 与我们联系。

## 许可证

此工具在 MIT 许可证下发布。有关更多信息，请查看 LICENSE 文件。
