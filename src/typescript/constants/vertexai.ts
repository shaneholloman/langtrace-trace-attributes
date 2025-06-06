/*
 * Copyright (c) 2024 Scale3 Labs
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

export const APIS = {
  GENERATE_CONTENT: {
    METHOD: "vertexAI.GenerativeModel.generateContent",
  },
  GENERATE_CONTENT_STREAM: {
    METHOD: "vertexAI.GenerativeModel.generateContentStream",
  },
  SEND_MESSAGE: {
    METHOD: "vertexAI.ChatSession.sendMessage",
  },
  SEND_MESSAGE_STREAM: {
    METHOD: "vertexAI.ChatSession.sendMessageStream",
  },
  START_CHAT: {
    METHOD: "vertexAI.ChatSession.startChat",
  },
} as const;
export type VertexAIFunctions = (typeof APIS)[keyof typeof APIS]["METHOD"];
export const VertexAIFunctionNames: VertexAIFunctions[] = Object.values(
  APIS
).map((api) => api.METHOD);
